# Project 04 - Movie Picture Pipeline

CI | CD |
--- | --- |
[![Backend Continuous Integration](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/backend-ci.yaml/badge.svg)](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/backend-ci.yaml) | [![Backend Continuous Deployment](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/backend-cd.yaml/badge.svg)](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/backend-cd.yaml) | 
[![Frontend Continuous Integration](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/frontend-ci.yaml/badge.svg)](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/frontend-ci.yaml) | [![Frontend Continuous Deployment](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/frontend-cd.yaml/badge.svg)](https://github.com/congdinh2008/aws-cloud-devops-udacity-prj4-pipeline/actions/workflows/frontend-cd.yaml) | 

- Project 04 - Movie Picture Pipeline](#udacity-aws-cloud-devops-engineer---project-04---movie-picture-pipeline)
  - [Deliverables](#deliverables)
    - [Frontend](#frontend)
    - [Backend](#backend)
  - [One-time setup instructions](#one-time-setup-instructions)
    - [Login](#login)
    - [Configuration](#configuration)
  - [Setting up Continuous Deployment environment](#setting-up-continuous-deployment-environment)
    - [Create AWS infrastructure with Terraform](#create-aws-infrastructure-with-terraform)
    - [Generate AWS access keys for Github Actions](#generate-aws-access-keys-for-github-actions)
    - [Add Github Action user to Kubernetes](#add-github-action-user-to-kubernetes)
  - [Dependencies](#dependencies)
  - [Frontend Development notes](#frontend-development-notes)
    - [Running tests](#running-tests)
    - [Running linter](#running-linter)
    - [Build and run](#build-and-run)
    - [Deploy Kubernetes manifests](#deploy-kubernetes-manifests)
  - [Backend Development notes](#backend-development-notes)
    - [Running tests](#running-tests-1)
    - [Running linter](#running-linter-1)
    - [Build and run](#build-and-run-1)
    - [Deploy Kubernetes manifests](#deploy-kubernetes-manifests-1)
  - [License](#license)

You have been appointed as a DevOps resource for the development team managing web applications in the Movies category. They are in desperate need of automating their development process in hopes of speeding up their release cycles. They wanted to use Github Actions to automate testing, building, and deploying their application to an existing Kubernetes cluster.

The team's project is comprised of 2 applications.

1. Frontend: Typescript, using the React framework
2. Backend: Python using the Flask framework.

You will find 2 folders, one named `frontend` and one named `backend`, where the source code of each application is maintained. Your job is to use the team's information and create a CI/CD pipeline to meet the team's needs.

### Frontend

1. A Continuous Integration workflow that:
   1. Runs on `pull_requests` against the `main` branch,only when code in the frontend application changes.
   2. Is able to be run on-demand (i.e. manually without needing to push code)
   3. Runs the following jobs in parallel:
      1. Runs a linting job that fails if the code doesn't adhere to eslint rules
      2. Runs a test job that fails if the test suite doesn't pass
   4. Runs a build job only if the lint and test jobs pass and successfully builds the application
2. A Continuous Deployment workflow that:
   1. Runs on `push` against the `main` branch, only when code in the frontend application changes.
   2. Is able to be run on-demand (i.e. manually without needing to push code)
   3. Runs the same lint/test jobs as the Continuous Integration workflow
   4. Runs a build job only when the lint and test jobs pass
      1. The built docker image should be tagged with the git sha
   5. Runs a deploy job that applies the Kubernetes manifests to the provided cluster.
      1. The manifest should deploy the newly created tagged image
      2. The tag applied to the image should be the git SHA of the commit that triggered the build

### Backend

1. A Continuous Integration workflow that:
   1. Runs on `pull_requests` against the `main` branch,only when code in the frontend application changes.
   2. Is able to be run on-demand (i.e. manually without needing to push code)
   3. Runs the following jobs in parallel:
      1. Runs a linting job that fails if the code doesn't adhere to eslint rules
      2. Runs a test job that fails if the test suite doesn't pass
   4. Runs a build job only if the lint and test jobs pass and successfully builds the application
2. A Continuous Deployment workflow that:
   1. Runs on `push` against the `main` branch, only when code in the frontend application changes.
   2. Is able to be run on-demand (i.e. manually without needing to push code)
   3. Runs the same lint/test jobs as the Continuous Integration workflow
   4. Runs a build job only when the lint and test jobs pass
      1. The built docker image should be tagged with the git sha
   5. Runs a deploy job that applies the Kubernetes manifests to the provided cluster.
      1. The manifest should deploy the newly created tagged image
      2. The tag applied to the image should be the git SHA of the commit that triggered the build