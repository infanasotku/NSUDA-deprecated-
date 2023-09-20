namespace ShellHandler;

/// <summary>
/// Provides cross-platform shell access.
/// </summary>
internal interface IShellHandler
{
    /// <summary>
    /// Run shell with <paramref name="command"/>.
    /// </summary>
    internal void Run(string command);
    
    /// <summary>
    /// Kill shell if it working.
    /// </summary>
    internal void Kill();
}