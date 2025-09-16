all: process_data
# A rule to fetch the data
fetch_data:
	@echo "--- Fetching data ---"
	bash ./fetch_data.sh
	@echo "--- Pipeline complete ---"
# A rule to clean up the generated files
clean:
	@echo "--- Cleaning up ---"
	rm -f breeds.json

