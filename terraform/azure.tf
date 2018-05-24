variable "resource_group_name" {}
variable "resource_group_location" {}
variable "failover_location" {}

resource "azurerm_resource_group" "rg" {
    name     = "${var.resource_group_name}"
    location = "${var.resource_group_location}"
}

resource "random_integer" "ri" {
    min = 10000
    max = 99999
}

resource "azurerm_cosmosdb_account" "db" {
    name                = "mcwhirter-cosmos-db-${random_integer.ri.result}"
    location            = "${azurerm_resource_group.rg.location}"
    resource_group_name = "${azurerm_resource_group.rg.name}"
    offer_type          = "Standard"
    kind                = "MongoDB"

    consistency_policy {
        consistency_level       = "Eventual"
    }

    geo_location {
        location          = "${azurerm_resource_group.rg.location}"
        failover_priority = 0
    }
}
