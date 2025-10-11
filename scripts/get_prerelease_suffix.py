#!/usr/bin/env python3

import re
import os


def set_prerelease_env():
    
    github_head_ref = os.getenv('NAME_BRANCH') 

    if not github_head_ref:
        print("❌ Error: The environment variable 'NAME_BRANCH' is not defined in the Job environment.")
        return

    name_branch = github_head_ref.lower()
    
    prerelease_match = re.findall("alpha|beta|prerelease", name_branch)

    if prerelease_match:
        prerelease_value = prerelease_match[0]
        
        env_file = os.getenv('GITHUB_ENV')
        
        if env_file:
            with open(env_file, "a") as myfile:
                myfile.write(f"PRERELEASE={prerelease_value}\n") 
            print(f"✅ 'PRERELEASE' variable successfully defined: {prerelease_value}")
        else:
            print("⚠️ WARNING: Environment variable 'GITHUB_ENV' not found. (Not running in GitHub Actions?)")
    else:
        print("⛔ No prerelease status found in the branch name. No variables defined.")


def main():
    set_prerelease_env()


if __name__ == '__main__':
    main()