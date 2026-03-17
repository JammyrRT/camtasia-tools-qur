import xml.etree.ElementTree as ET
import os

class CamtasiaMetadataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.metadata = {}

    def extract_metadata(self):
        # Check if the file exists
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            self._parse_metadata(root)
        except ET.ParseError as e:
            raise ValueError(f"Error parsing XML: {e}")

    def _parse_metadata(self, root):
        # Extract relevant metadata
        self.metadata['project_name'] = root.findtext('.//projectName', default='Unknown Project')
        self.metadata['version'] = root.findtext('.//version', default='Unknown Version')
        self.metadata['author'] = root.findtext('.//author', default='Unknown Author')
        
        # TODO: Add more metadata extraction as needed
        # This is a minimal example; consider extracting more fields from the XML structure.

    def get_metadata(self):
        return self.metadata

    def display_metadata(self):
        # Display the extracted metadata in a human-readable format
        print("Camtasia Project Metadata:")
        for key, value in self.metadata.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

if __name__ == "__main__":
    # TODO: Add command-line interface for user input
    sample_file = "example.tscproj"  # Replace with actual file path
    extractor = CamtasiaMetadataExtractor(sample_file)
    
    try:
        extractor.extract_metadata()
        extractor.display_metadata()
    except Exception as e:
        print(f"An error occurred: {e}")
