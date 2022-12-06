resource "helm_release" "helm_external_dns" {

    name = "external-dns"
    repository = "https://charts.bitnami.com/bitnami"
    chart = "external-dns"
    version = "6.12.0"

    values = [
        "${file("external-dns-values.yaml")}"
    ]
}
