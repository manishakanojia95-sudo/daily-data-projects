name: Daily Project Generator

on:
  workflow_dispatch:

jobs:
  generate-project:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: List files (debug)
        run: |
          echo "Current directory:"
          pwd
          echo "Files:"
          ls -la

      - name: Run Python script
        run: python3 generate_project.py

      - name: Commit and push changes
        run: |
          git config --global user.name "Manisha Kanojia"
          git config --global user.email "manishakanojia95@gmail.com"
          git add .
          git commit -m "Auto project" || echo "Nothing to commit"
          git push
