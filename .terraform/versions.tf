terraform {
  required_providers {
    # https://registry.terraform.io/providers/databricks/databricks/latest/docs
    databricks = {
      source  = "databricks/databricks"
      version = "1.30.0"
    }
  }
}
