import hashlib
import requests

def get_pwned_data(prefix: str) -> list[str]:
    """Consulta a API do Have I Been Pwned com o prefixo SHA1."""
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao consultar a API do HIBP: {e}")
        return []
    return response.text.splitlines()

def is_password_compromised(password: str) -> bool:
    """Verifica se a senha foi exposta em vazamentos."""
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    leaked_hashes = get_pwned_data(prefix)

    for entry in leaked_hashes:
        hash_suffix, count = entry.split(":")
        if hash_suffix == suffix:
            print(f"🔴 Senha encontrada {count} vezes em vazamentos!")
            return True

    print("🟢 Senha NÃO encontrada em vazamentos.")
    return False

def show_manual_email_checks(email: str):
    """Exibe links para verificar vazamento do e-mail manualmente."""
    print("\n🔎 Verificação manual para o e-mail:\n")
    print(f"1. Mozilla Monitor:\n   https://monitor.firefox.com/?email={email}")
    print(f"2. F-Secure Identity Theft Checker:\n   https://www.f-secure.com/en/identity-theft-checker/email/{email}")

def main():
    email = input("Digite o e-mail para verificar: ").strip()
    password = input("Digite a senha para verificar: ").strip()

    if not email or not password:
        print("⚠️  E-mail e senha são obrigatórios.")
        return

    print(f"\n📬 Verificando dados para: {email}")
    show_manual_email_checks(email)

    print("\n🛡️ Verificando segurança da senha com a base pública do HIBP...")
    is_password_compromised(password)

    print("\n🧪 Verificação adicional no Cybernews:")
    print(f"https://cybernews.com/breaches/search/?q={password}")

if __name__ == "__main__":
    main()
