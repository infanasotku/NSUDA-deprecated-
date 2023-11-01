using Microsoft.AspNetCore.DataProtection.AuthenticatedEncryption.ConfigurationModel;

namespace NSUDA.API
{
    internal class NSUDAAPI : IAPI
    {
        async Task IAPI.HandleRequest(HttpContext context)
        {
            throw new NotImplementedException();
        }

        private async Task GetConfig(string email)
        {
            throw new NotImplementedException();
        }
    }
}