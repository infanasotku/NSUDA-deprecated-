namespace Xray;

/// <summary>
/// Provides functions for interacting with the file system.
/// </summary>
internal static class Utils
{
    internal static async Task CopyFileToAppDataDirectory(string filename, string path)
	{
		// Open the source file
		using Stream inputStream = await FileSystem.Current.OpenAppPackageFileAsync(filename);

		// Create an output filename
		string targetFile = Path.Combine(FileSystem.Current.AppDataDirectory, path);
		targetFile = Path.Combine(targetFile, filename);

		// Copy the file to the AppDataDirectory
		if (!Directory.Exists(Path.Combine(FileSystem.Current.AppDataDirectory,
				path)))
		{
			Directory.CreateDirectory(Path.Combine(FileSystem.Current.AppDataDirectory,
				path));
		}
		using FileStream outputStream = File.Create(targetFile);
		await inputStream.CopyToAsync(outputStream);
	}
}