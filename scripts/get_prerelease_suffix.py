#!/usr/bin/env python3

import re
import os


def set_prerelease_env():
    
    github_head_ref = os.getenv('NAME_BRANCH') 

    if not github_head_ref:
        print("Erro: A variável de ambiente NAME_BRANCH não está definida no ambiente do Job.")
        return

    name_branch = github_head_ref.lower()
    
    prerelease_match = re.findall("alpha|beta|prerelease", name_branch)

    if prerelease_match:
        prerelease_value = prerelease_match[0]
        
        env_file = os.getenv('GITHUB_ENV')
        
        if env_file:
            with open(env_file, "a") as myfile:
                myfile.write(f"PRERELEASE={prerelease_value}\n") 
            print(f"Variável PRERELEASE definida com sucesso: {prerelease_value}")
        else:
            print("AVISO: Variável de ambiente GITHUB_ENV não encontrada. (Não executando em GitHub Actions?)")
    else:
        print("Nenhum status de prerelease encontrado no nome do branch. Nenhuma variável definida.")


def main():
    set_prerelease_env()


if __name__ == '__main__':
    main()