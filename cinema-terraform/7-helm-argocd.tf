resource "helm_release" "helm_argo_cd" {

    name = "argo-cd"
    repository = "https://argoproj.github.io/argo-helm"
    chart = "argo-cd"
    version = "5.9.1"

    values = [
        "${file("argo-values.yaml")}"
    ]
}
