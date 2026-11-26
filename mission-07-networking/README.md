# Mission 7 — How computers communicate

## 1. Task / objective
Explain core computer networking concepts (`LAN`, `MAN`, `WAN`, `DNS`, `Router`, `Protocol`, `Packet switching`, `Client-server`), perform privacy-safe connectivity and DNS lookup tests from Terminal, and describe what happens step-by-step when opening a website in a browser.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| LAN (Local Area Network) | A network linking nearby devices inside a single room, home, lab, or office building. | Devices connected to the same home Wi-Fi router or college computer lab switch. |
| MAN (Metropolitan Area Network) | A medium-scale network connecting buildings or campuses across a city or large university area. | A city-wide cable network or multi-block university campus fiber network. |
| WAN (Wide Area Network) | A large-scale network spanning cities, countries, or continents by linking smaller networks together. | The public Internet connecting servers and users worldwide. |
| DNS (Domain Name System) | A directory service that translates human-readable domain names into numerical IP addresses. | Turning `example.com` into `172.66.147.243`. |
| Router | A networking device that connects separate networks and forwards data packets toward their destination IP. | A home Wi-Fi router forwarding requests between a local LAN and the ISP's WAN. |
| Protocol | An agreed set of rules and formats that devices follow so they can understand each other's messages. | `HTTPS` (secure web pages), `DNS` (name lookup), and `TCP/IP` (reliable packet delivery). |
| Packet switching | Splitting messages into small numbered packets that travel independently across the network and are reassembled at the destination. | Downloading a web page as separate IP packets routed across multiple links. |
| Client-server | A communication model where a client program initiates a request for a resource and a server program processes and sends back the response. | A web browser (client) requesting a page from a web server hosting `example.com`. |

### Task 7.2 — Observe network information
Ran connectivity and DNS checks against the public domain `example.com` (keeping personal/local network details private):
- **Connectivity test (`ping -c 3 example.com`):** Sent 3 ICMP echo packets to `example.com` (`172.66.147.243`) and received all 3 replies (`0.0% packet loss`, average round-trip time `11.131 ms`).
- **DNS lookup (`nslookup example.com`):** Returned non-authoritative IPv4 addresses `104.20.23.154` and `172.66.147.243` for `example.com` via DNS resolver `8.8.8.8#53`.

**Questions and answers:**
- **What a connectivity test helps you check:** `ping` verifies whether your computer has an active network path to a remote host, whether packets are being dropped (`packet loss`), and how long a round-trip message takes (`latency` in milliseconds).
- **What information a DNS lookup displays:** `nslookup` displays which DNS resolver answered the query and the IP address(es) currently mapped to the requested domain name (`example.com` resolved to `104.20.23.154` and `172.66.147.243`).
- **Role of DNS when you enter a website name in a browser:** Browsers need an IP address to route packets across the Internet, not just an English name; DNS looks up the domain name behind the scenes and supplies the server's IP address so the browser can connect.

### Task 7.3 — What happens when you open a website?
1. **User enters URL in the client:** You type `https://example.com` into your web browser, which acts as the **client** requesting a web resource.
2. **DNS lookup resolves the domain:** The browser checks its local cache and, if needed, sends a **DNS** query (using the DNS **protocol**) to find the IP address for `example.com` (for example, `172.66.147.243`).
3. **Connection travels through the router:** Using the resolved IP address, the client sends connection packets through your local network **router**, which forwards them across ISP networks toward the destination network.
4. **Protocol handshake and request:** The client and remote **server** establish a reliable connection using the `TCP` **protocol** (and encrypt the session with `TLS`), then the browser sends an `HTTPS` GET request asking for the page.
5. **Server prepares and returns packets:** The **server** hosting `example.com` processes the request and sends back the HTML page (along with status code `200 OK`) split into network packets.
6. **Client reassembles and renders the response:** Your browser receives the packets, checks they arrived intact, interprets the HTML/CSS response, and displays the web page on your screen.

## 3. Commands / tools used
- `ping -c 3 example.com` — Sends 3 test packets to check reachability, packet loss, and round-trip latency.
- `nslookup example.com` — Queries DNS to discover the IP addresses associated with `example.com`.

## 4. My understanding
Opening a web page relies on layered teamwork between naming (`DNS`), routing (`routers` and `packet switching`), and standardized `protocols` (`TCP/IP`, `HTTPS`) inside a `client-server` model. Because humans remember domain names while networks route by numeric IP addresses, DNS bridges the gap automatically before the browser ever requests the page from the server.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- Network test output (public `example.com` only): `../evidence/mission-07-network-output.txt`
- `README.md` (network concepts table, observations, and 6-step website walkthrough)

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Status:** Committed and pushed to `origin/main` on GitHub.
