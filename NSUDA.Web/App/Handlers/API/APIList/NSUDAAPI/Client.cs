
namespace NSUDA.API
{
    using Newtonsoft.Json;
    internal class Client
    {
        internal class Inbound
        {
            [JsonProperty("listen")]
            internal readonly string Listen;
            [JsonProperty("port")]
            internal readonly int Port;
            [JsonProperty("protocol")]
            internal readonly string Protocol;
            [JsonProperty("tag")]
            internal readonly string Tag;

            internal Inbound()
            {
                Listen = "127.0.0.1";
                Port = 2080;
                Protocol = "socks";
                Tag = "socks-in";
            }
        }


    }
}