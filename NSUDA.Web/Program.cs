using Microsoft.AspNetCore.HttpOverrides;
using NSUDA.Handler;
using NSUDA.API;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
if (!app.Environment.IsDevelopment())
{
    app.UseHttpsRedirection();
    app.UseForwardedHeaders(new ForwardedHeadersOptions
    {
        ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
    });
}       


RegistrationHandler.RegistrateAll(app);

app.UseAPI();
app.UseStaticFiles();
app.Run();
