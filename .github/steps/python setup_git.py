import os

# Налаштування користувача
user_name = "Dmytro Ivanov"  # Замініть на своє ім'я
user_email = "dmytro.ivanov@example.com"  # Замініть на свою email-адресу
repo_name = "my_new_repo"  # Назва нового репозиторію

# Налаштування Git користувача
os.system(f'git config --global user.name "{user_name}"')
os.system(f'git config --global user.email "{user_email}"')

# Створення нового репозиторію
os.system(f'mkdir {repo_name}')
os.chdir(repo_name)
os.system('git init')

# Створення першого коміту
with open("README.md", "w") as f:
    f.write(f"# {repo_name}\n\nРепозиторій створено та ініціалізовано.")

os.system('git add README.md')
os.system('git commit -m "Initial commit"')

print("Git налаштовано, репозиторій створено та виконано перший коміт.")