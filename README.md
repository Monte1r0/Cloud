# 🔐 LeakCheck - Verificador de Vazamento de Credenciais

Este script em Python realiza uma verificação de segurança básica para saber se uma **senha** ou **e-mail** foi comprometido em vazamentos de dados conhecidos.

## 📌 Funcionalidades

- Verifica se uma **senha** foi encontrada em vazamentos públicos usando a API oficial do [Have I Been Pwned (HIBP)](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange).
- Fornece links para verificar **manualmente** se um e-mail foi vazado (Mozilla Monitor e F-Secure).
- Gera um link para pesquisa adicional no banco de dados da **CyberNews**.

## 🛠️ Como Usar

1. **Pré-requisitos:**
   - Python 3.7+
   - Biblioteca `requests` instalada:  
     ```bash
     pip install requests
     ```

2. **Execução do Script:**
   ```bash
   python leakcheck.py <email> <senha>


3. **Execução do Script:**
   ```Docker
   docker run -t samuelmonteiroacr.azurecr.io/leakcheck:v1 <email> <senha>

