namespace ShellHandler;

/// <summary>
/// Provides create of ShellHandler.
/// </summary>
internal class ShellHandlerCreator
{
    /// <summary>
    /// Create shell for current Platform.
    /// </summary>
    /// <exception cref="InvalidOperationException"></exception>
    internal static IShellHandler BuildShell()
    {
        if (DeviceInfo.Platform == DevicePlatform.macOS)
        {
            return new MacShellHandler();
        }
        else
        {
            throw new InvalidOperationException("Bad Platform");
        }
    }
}