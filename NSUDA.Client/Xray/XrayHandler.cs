using ShellHandler;

namespace XrayHandler;

/// <summary>
/// Provides Xray manage functionality.
/// </summary>
internal class XrayHandler
{
    /// <summary>
    /// Cross-platform shell.
    /// </summary>
    private IShellHandler _shell;

    /// <summary>
    /// Empty if running successfully ended
    /// and error message otherwise.
    /// </summary>
    public string ErrorMsg { get; set; }

    /// <summary>
    /// Current mail for user.
    /// </summary>
    public string Email { get; set; }

    internal XrayHandler()
    {
        _shell = ShellHandlerCreator.BuildShell();
        Email = "";
    }

    private bool ValidateEmail()
    {
        var trimmedEmail = Email.Trim();

        if (trimmedEmail.EndsWith(".")) {
            return false;
        }
        try {
            var addr = new System.Net.Mail.MailAddress(Email);
            return addr.Address == trimmedEmail;
        }
        catch {
            return false;
        }
    }
    
    /// <summary>
    /// <para>Run Xray on current platform.</para>
    /// Put error to <see cref="ErrorMsg"/> if running ended
    /// with an error  
    /// </summary>
    /// <returns>False if the running ended with an error 
    /// and true otherwise.</returns>
    /// <exception cref="InvalidOperationException"></exception>
    internal async Task<bool> Run()
    {
        ErrorMsg = "";
        if (ValidateEmail())
        {
            ErrorMsg = "Bad email";
            return false;
        }
        if (!await CheckAuthState())
        {
            ErrorMsg = "This email doesn't exist";
            return false;
        }
        
        if (DeviceInfo.Platform == DevicePlatform.macOS)
        {
            RunOnMac();
        }
        else
        {
            throw new InvalidOperationException("Bad Platform");
        }
        return true;
    }

    private async Task<bool> CheckAuthState()
    {
        throw new NotImplementedException();
    }

    private async Task GetConfig()
    {
        throw new NotImplementedException();
    }

    /// <summary>
    /// Run Xray on MacOS.
    /// </summary>
    private void RunOnMac()
    {
        throw new NotImplementedException();
    }



}