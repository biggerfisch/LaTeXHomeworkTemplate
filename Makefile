.PHONY: save all clean

save:
	pip freeze -r requirements_to_freeze.txt > requirements.txt


