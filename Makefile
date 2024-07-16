local-setup:
	@echo "Creating virtual environment"
	@python -m venv network_simulator_core_env
	@echo "Activating virtual environment"
	@source network_simulator_core_env/bin/activate
	@echo "Upgrading pip"
	@pip install --upgrade pip

requirements:
	@echo "Installing requirements"
	@pip install -r requirements.txt

unit-tests:
	@echo "Running tests"
	@python -m pytest tests/