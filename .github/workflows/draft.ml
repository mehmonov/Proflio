name: Deploy to Timeweb

on:
  push:
    branches:
      - master
  pull_request:
    types:
      - closed

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' || (github.event_name == 'pull_request' && github.event.pull_request.merged == true)
    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install wheel
        pip install Cython
        pip install -r requirements.txt

    - name: Deploy to server
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        password: ${{ secrets.PASSWORD }}
        key: ${{ secrets.SSH_PRIVATE_KEY }}
        script: |
          eval $(ssh-agent -s)
          echo "${{ secrets.SSH_PRIVATE_KEY }}" | ssh-add -
          ssh-keyscan -H github.com >> ~/.ssh/known_hosts
          cd /home/
          if [ ! -d "${{ secrets.PROJECT_NAME }}" ]; then
            git clone git@github.com:mehmonov/${{ secrets.PROJECT_NAME }}.git
          else
            cd /home/${{ secrets.PROJECT_NAME }}
            git pull origin main
          fi
          cd /home/${{ secrets.PROJECT_NAME }}
          git fetch origin main
          git reset --hard origin/main
          python3 -m venv venv
          source venv/bin/activate
          pip install --upgrade pip
          pip install wheel
          pip install Cython
          pip install -r requirements.txt
          sudo apt-get update
          sudo apt-get install -y $(cat requirements_server.txt | cut -d'=' -f1)
          python manage.py migrate
          python manage.py collectstatic --noinput
          sudo supervisorctl restart all
          sudo systemctl reload nginx