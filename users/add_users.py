"""
Gives users access to the kubeflow UI
https://finantier-team.atlassian.net/wiki/spaces/PLAT/pages/69468184/Full+Kubeflow+deployment

"""
import subprocess

PROJECT = "finantier-credit-score"

users = [
    "leonard@finantier.co",
    "sijie@finantier.co",
    "rubenstefanus@finantier.co",
    "fregy@finantier.co",
    "richardng@finantier.co",
    "aaronfoo@finantier.co",
]

for user in users:
    cmd = ["gcloud", "projects", "add-iam-policy-binding", PROJECT, f"--member=user:{user}" , "--role=roles/iap.httpsResourceAccessor"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
