
# README

Project to showcase possibilities to link mulitple gcp cloud functions with docker and debug them using vscode.

## How to use

Run the `Server\Client` configuration from the VSCode run and debug dropdown

- the task will build the images and will create a container
- `functions-framework` is used to interact locally with the cloud functions

## Docker commands

### Build and run functionA

`docker build gcp-functionA -t functiona`\
`docker run -p 8081:8080 functiona`

### Build and run functionB

`docker build gcp-functionB -t functionb`\
`docker run -p 8080:8080 functionb`
