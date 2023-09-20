namespace ShellHandler;
using ToolBox.Bridge;
using System.Diagnostics;

internal class MacShellHandler : IShellHandler
{
    private static IBridgeSystem _bridgeSystem;
    private static Process _currentProcess;
    

    internal MacShellHandler()
    {
		_bridgeSystem = BridgeSystem.Bash;
        ((IShellHandler)this).Run("chmod +x cmd.sh");
    }

    void IShellHandler.Run(string command)
    {
        string[] array = _bridgeSystem.CommandConstructor(command, Output.Hidden, "");


        ProcessStartInfo processStartInfo = new ProcessStartInfo();


        processStartInfo.FileName = _bridgeSystem.GetFileName();
        for (int i = 0; i < array.Length; i++)
        {
            processStartInfo.ArgumentList.Add(array[i]);
        }

        processStartInfo.RedirectStandardInput = false;
        processStartInfo.UseShellExecute = false;

        _currentProcess = Process.Start(processStartInfo)!;
    }

    void IShellHandler.Kill()
    {
        _currentProcess.Kill();
    }

}