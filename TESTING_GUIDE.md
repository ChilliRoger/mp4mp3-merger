# Testing Guide

This guide will help you test the MP4/MP3 Merger application.

## Prerequisites

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install FFmpeg** (required by MoviePy):
   - Windows: Download from https://ffmpeg.org/download.html
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

3. **Prepare test files** (optional but recommended):
   - `test_video.mp4` - A small MP4 video file for testing
   - `test_audio.mp3` - An MP3 audio file for testing

## Testing Methods

### Method 1: Automated Test Suite

Run the automated test script:

```bash
python test_app.py
```

This will test:
- ✓ Server connectivity
- ✓ Homepage loading
- ✓ Static directory creation
- ✓ Error handling
- ✓ File upload and merge (if test files are available)

### Method 2: Manual Browser Testing

1. **Start the server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

3. **Test scenarios**:

   **Scenario 1: Normal Operation**
   - Upload a valid MP4 video file
   - Upload a valid MP3 audio file
   - Click "Merge & Download"
   - Verify the merged file downloads successfully

   **Scenario 2: Missing Files**
   - Try to submit the form without selecting files
   - Verify the form doesn't crash

   **Scenario 3: Invalid Files** (if possible)
   - Try uploading non-MP4/MP3 files
   - Verify error handling

### Method 3: Command Line Testing (with curl)

If you have test files, you can test via command line:

```bash
curl -X POST http://localhost:5000 \
  -F "video=@test_video.mp4" \
  -F "audio=@test_audio.mp3" \
  --output merged_output.mp4
```

## Expected Behavior

### Successful Merge
- Files are uploaded
- Processing takes some time (depends on file size)
- Merged MP4 file downloads automatically
- No errors in console

### Error Cases
- Missing files: Form should reload without crashing
- Invalid files: Should handle gracefully (may show error in logs)
- Large files: May timeout or take very long

## Troubleshooting Tests

### Test Script Can't Connect
- **Issue**: "Server is not running"
- **Solution**: Start the server first with `python app.py`

### Test Files Not Found
- **Issue**: "Test video/audio file not found"
- **Solution**: Create or download small test MP4 and MP3 files, or skip upload tests

### FFmpeg Errors
- **Issue**: MoviePy can't find FFmpeg
- **Solution**: Install FFmpeg and ensure it's in your system PATH

### Import Errors
- **Issue**: Module not found
- **Solution**: Run `pip install -r requirements.txt`

## Performance Testing

For performance testing, try with different file sizes:

1. **Small files** (< 10MB): Should process quickly
2. **Medium files** (10-50MB): May take 30 seconds to 2 minutes
3. **Large files** (50-100MB): May take several minutes

**Note**: Processing time depends on:
- File size
- System CPU and memory
- FFmpeg performance

## Checking Logs

The application logs errors and important events. Check the console output when running `python app.py` for:
- File upload confirmations
- Processing progress
- Error messages
- Cleanup operations

## Next Steps After Testing

If tests pass:
1. Review the `PROJECT_ANALYSIS.md` for detailed insights
2. Consider improvements mentioned in the analysis
3. Test with real-world file sizes
4. Consider deployment options

If tests fail:
1. Check error messages in console
2. Verify all dependencies are installed
3. Ensure FFmpeg is properly installed
4. Check file permissions for static directory

