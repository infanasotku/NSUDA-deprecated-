namespace NSUDA.Handler
{
    using System.Reflection;

    /// <summary>
    /// Provides functional for register <see cref="RequestDelegate"/> methods.
    /// </summary>
    internal static partial class RegistrationHandler
    {
        /// <summary>
        /// Register the all methods with HandlerPath attribute.
        /// Start the all register methods from this class.
        /// </summary>
        internal static void RegistrateAll(WebApplication application)
        {
            MethodInfo[] handlers = typeof(Handler).GetMethods(
                BindingFlags.NonPublic
                | BindingFlags.Static
            );

            foreach (var handler in handlers)
            {
                Attribute? attribute = 
                    Attribute.GetCustomAttribute(handler, typeof(HandlerPathAttribute));
                if (attribute is HandlerPathAttribute attr)
                {
                    application.Map(attr.path, async(context) => 
                    {
                        object[] param = new object[] { context };
                        await (Task)handler?.Invoke(null, param)!;
                    });
                }
            }

            MethodInfo[] registrationHandlers = 
                typeof(RegistrationHandler).GetMethods(
                BindingFlags.NonPublic
                | BindingFlags.Static);

            foreach (var handler in registrationHandlers)
            {
                if (handler.Name != "RegistrateAll")
                {
                    object[] param = new object[] { application };
                    try
                    {
                        handler?.Invoke(null, param);
                    }
                    catch
                    {
                        throw new ArgumentException("Bad resgistrate function");
                    }
                }
            }
        }
    }



}