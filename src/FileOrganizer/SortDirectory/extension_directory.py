class extension_directory:
    def __init__(self):
        self.file_directory = {
            "txt" : "Document",
            "Doc" : "Document",
            "Docx" : "Document",
            "Epub" : "Document",
            "HTML" : "Document",
            "Mobi" : "Document",
            "pdf" : "Document",
            "7Z" : "Archives",
            "Tar" : "Archives",
            "War" : "Archives",
            "Zip" : "Archives",
            "Jar" : "Application",
            "Py" : "Application",
            "exe" : "Application",
            "mp3" : "Videos",
            "mp4" : "Videos"
        }
    def get_directory(self):
        return self.file_directory