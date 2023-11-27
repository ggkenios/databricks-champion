variable "databricks_host" {
  type        = string
  default     = null
  description = "The Databricks host."
}

variable "databricks_token" {
  type        = string
  default     = null
  sensitive   = true
  description = "The Databricks token."
}

variable "git_username" {
  type        = string
  default     = null
  description = "A map of maps for each git repository's configurations."
}

variable "git_provider" {
  type        = string
  default     = null
  description = "The git provider. Eg: gitHub, azureDevOpsServices, gitLab"
}

variable "git_token" {
  type        = string
  default     = null
  sensitive   = true
  description = "The token to access the git repository."
}
