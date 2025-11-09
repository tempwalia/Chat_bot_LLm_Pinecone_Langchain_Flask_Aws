cat > structure.sh << 'EOF'
mkdir -p src
mkdir -p analysis

touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch .env
touch setup.py
touch README.md
touch app.py
touch analysis/trials.ipynb
touch requirements.txt

echo "Directory and files are successfully created"
EOF