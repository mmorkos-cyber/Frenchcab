FROM python:3.11

# Dossier de travail dans le conteneur
WORKDIR /backend

# Installer les dépendances
RUN apt-get install -y python3 python3-pip && 

# Copier le reste du projet
COPY requirements.txt ./
RUN pip install -r requirements.txt && rm requirements.txt

# Copier le dossier 
COPY backend .

# Exposer le port de l'API
EXPOSE 3000

# Lancer l'application
CMD ["run", "python", "--host", "0.0.0.0", "--port", "3000"]
