FROM python:3.10-bullseye

# Set the working directory globally
ARG SOURCEDIR="app"
ARG APP_NAME="photogram"

# Configure Python to not buffer "stdout" or create .pyc files
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Add a non-root user for security reasons
RUN adduser --home /${SOURCEDIR} ${APP_NAME}
USER photogram

# Ensure the binaries are accessible and executable
ENV PATH=/${SOURCEDIR}/.local/bin:$PATH

# Perform a healthcheck to ensure the service is up and running
HEALTHCHECK --interval=20m --timeout=3s --retries=3 \
  CMD curl --include --request GET http://localhost:5000/health || exit 1

WORKDIR /home/${APP_NAME}/${SOURCEDIR}

COPY ./requirements.txt .

RUN pip install -r /home/${APP_NAME}/${SOURCEDIR}/requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "config:app", "--host=0.0.0.0", "--port=5000"]