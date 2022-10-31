# lincoln_exercise
Exercise given by a consultant company for a data engineering application

To execute the code with Docker:
docker build --tag lincoln_exercise .
docker run -ti lincoln_exercise

To save the Docker image:
docker save lincoln_exercise -o lincol_exercise.tar

To execute the code locally without Docker
pip install -r requirements.txt
python logic/main.py
