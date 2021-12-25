## codecommit

### create repo

`aws codecommit create-repository --repository-name foobar`

### list all repos

`aws codecommit list-repositories`

### get repository info

`aws codecommit get-repository --repository-name foobar`

get clone url

`aws codecommit get-repository --repository-name foobar | jq '.repositoryMetadata.cloneUrlHttp'`
