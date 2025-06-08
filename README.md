
# Projeto de API com Azure API Management (APIM) e Azure AD

Este repositório documenta os principais conceitos, configurações e práticas aplicadas durante o desenvolvimento de uma API protegida e publicada com o **Azure API Management (APIM)** e **Azure Active Directory (Azure AD)**.

---

## 🧱 1. Azure API Management (APIM)

### 🛡️ API Gateway
O APIM atua como um gateway, expondo e protegendo as APIs. Ele controla o tráfego, aplica políticas e fornece um ponto de entrada único para os consumidores.

### 🔁 Versionamento
Foi adotada uma estratégia de versionamento via URL (`/v1/`, `/v2/`), permitindo evoluir a API sem impactar consumidores existentes.

### 🔄 Fluxos Inbound e Outbound
- **Inbound:** autenticação, validação, CORS, logging.
- **Outbound:** formatação da resposta, remoção de headers sensíveis.

### 🧾 Policy
As **políticas** são scripts XML aplicados ao pipeline da API. Foram utilizadas para:
- Validar JWT
- Aplicar CORS
- Inserir headers personalizados
- Controlar o tráfego

### 🔑 Subscription Key
As APIs são protegidas por **chaves de subscrição**, gerenciadas dentro do APIM. A chave deve ser enviada no header `Ocp-Apim-Subscription-Key`.

### 📦 Organização de Produtos
Um **produto** no APIM pode conter várias APIs. Foi criado um produto para agrupar APIs internas, facilitando a gestão de acesso e publicação.

### 🔐 JWT (JSON Web Token)
A autenticação das requisições é feita via tokens JWT, emitidos pelo Azure AD e validados por policies no APIM.

---

## 🔐 2. Azure Active Directory (Azure AD)

### 🧾 App Registration
Foi feito o registro de um **aplicativo** no Azure AD para emissão de tokens OAuth 2.0. Este app representa o consumidor autorizado da API.

### 📛 Client ID & Secret
- **Client ID:** identifica o aplicativo registrado.
- **Secret:** credencial segura usada para autenticação do cliente.

### 🔓 OpenID Connect
O APIM utiliza **OpenID Connect** para validar tokens JWT emitidos pelo Azure AD.

### 👥 Roles
O app registration possui **roles** customizadas para controle de acesso. Usuários ou apps podem ser atribuídos a essas funções.

---

## ⚙️ 3. Web-App (Aplicação Backend da API)

### 🌍 CORS Restritivo
A API responde apenas a requisições originadas do domínio da **APIM**. Isso é feito para proteger contra requisições maliciosas e garantir segurança no frontend.

