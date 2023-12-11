# .github/workflows/display-greeting.yml
name: Display Greeting

on:
  push:
    branches:
      - main

jobs:
  display-greeting:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Test My Name Action
        id: test-my-name
        uses: your-github-username/TestMyName_actions@main
        with:
          name: 'John'  # Replace with your desired name

      - name: Display Greeting
        run: echo "The greeting is ${{ steps.test-my-name.outputs.greeting }}"
