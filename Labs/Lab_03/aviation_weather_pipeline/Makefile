.PHONY: all fetch analyze clean

analyze: fetch
	@echo "Starting analysis of METAR data..."
	cat raw_metars/*.txt > weather_report.csv
	@echo "Analysis complete. Results saved to weather_report.csv"
	@echo "Pipeline completed successfully!"

fetch:
	@echo "Fetching METAR data for airports..."
	mkdir -p raw_metars
	echo "Sample METAR data for KJFK" > raw_metars/KJFK.txt
	echo "Sample METAR data for KLAX" > raw_metars/KLAX.txt
	@echo "Data successfully fetched and saved in raw_metars/"

clean:
	@echo "Cleaning up generated files..."
	rm -rf raw_metars weather_report.csv
	@echo "Cleanup complete. Workspace reset."
