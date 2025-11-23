# MP4/MP3 Merger

A Flask web application that merges MP4 video files with MP3 audio files into a single MP4 output.

## Features

- Upload MP4 video and MP3 audio files
- Merge them into a single MP4 file
- Download the merged result
- Automatic cleanup of temporary files

## Requirements

- Python 3.7+
- FFmpeg (required by MoviePy)
- Flask 3.0.3
- MoviePy 1.0.3

## Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install FFmpeg:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg` or `sudo yum install ffmpeg`

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Upload your MP4 video and MP3 audio files
4. Click "Merge & Download" to process and download the merged file

## Testing

Run the test suite:
```bash
python test_app.py
```

**Note**: For full testing, you'll need test MP4 and MP3 files named `test_video.mp4` and `test_audio.mp3` in the project directory. The test script will skip upload tests if these files are not found.

## Project Structure

```
mp4mp3-merger/
├── app.py                  # Main Flask application
├── test_app.py            # Test suite
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Web interface
├── vercel.json            # Vercel deployment config
├── PROJECT_ANALYSIS.md    # Detailed project analysis
└── static/                # Created automatically
    └── merged/            # Output directory
```

## Deployment

This project is configured for Vercel deployment. However, note that:
- Vercel has execution time limits that may be exceeded for large video files
- FFmpeg must be available in the deployment environment
- Consider using a dedicated server for production use

## Limitations

- Maximum file size: 100MB per file
- Processing time depends on file size and system resources
- Output files are not automatically cleaned up after download

## Troubleshooting

- **Import errors**: Make sure all dependencies are installed
- **FFmpeg errors**: Ensure FFmpeg is installed and in your system PATH
- **File upload fails**: Check file size (must be under 100MB)
- **Merge fails**: Verify both files are valid MP4/MP3 formats

## License

This project is open source and available for use.

