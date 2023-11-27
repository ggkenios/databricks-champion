resource "databricks_git_credential" "main" {
  git_username          = var.git_username
  git_provider          = var.git_provider
  personal_access_token = var.git_token
  force                 = true
}
