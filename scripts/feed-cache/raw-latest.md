# Raw feed pull — 2026-11-17 00:37 UTC

- Window: last 14h
- Feeds: 26 (25 ok, 0 empty, 1 error)
- Items kept after dedup: 63 (seen-skipped: 0, near-dup-skipped: 0)

## Feed health

- [OK] The Hacker News (4 items)
- [OK] BleepingComputer (11 items)
- [OK] Krebs on Security (0 items)
- [OK] Dark Reading (4 items)
- [OK] The Record (Recorded Future) (5 items)
- [OK] SecurityWeek (8 items)
- [ERR] SentinelOne Labs (0 items) — HTTP 404
- [OK] Cisco Talos (0 items)
- [OK] Unit 42 (Palo Alto) (1 items)
- [OK] Flashpoint (1 items)
- [OK] PortSwigger Research (0 items)
- [OK] Trail of Bits (0 items)
- [OK] Google Project Zero (0 items)
- [OK] Securelist (Kaspersky GReAT) (0 items)
- [OK] OpenAI Blog (3 items)
- [OK] Google DeepMind (0 items)
- [OK] Google AI Blog (1 items)
- [OK] Hugging Face Blog (0 items)
- [OK] TechCrunch AI (13 items)
- [OK] Simon Willison (1 items)
- [OK] Lilian Weng (OpenAI) (0 items)
- [OK] The Verge AI (10 items)
- [OK] AWS Security Blog (0 items)
- [OK] AWS News Blog (1 items)
- [OK] Google Cloud Security (0 items)
- [OK] CISA Alerts (0 items)

## Items

### 1. llm 0.37.3
- Section: AI — News & Analysis
- Source: Simon Willison
- URL: https://simonwillison.net/2026/Nov/16/llm/
- Published: 2026-11-16T23:57:26+00:00
- Summary: Release: llm 0.37.3
        A bug fix release for LLM, mainly to cover a problem with the most recent Homebrew package of the software.
Homebrew now ships the latest SQLite, 3.54.1, which includes a fix that broke LLM's logging code.
Short version: in SQLite 3.54.0 the following SQL:
select json_object('a', (select json_array(1)))

Returns this:
{"a":[1]}

But in 3.54.1 the same query returns this:
{"a":"[1]"}

According to D. Richard Hipp:

That was a bug fix. Per the documentation, (SELECT json_array(...)) returns SQL text, not JSON. Hence the 3.54.1 behavior is correct and 3.54.0 was a bug.

### 2. Cybersecurity AI startup Corma reaches $1B valuation in about 3 months
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/cybersecurity-ai-startup-corma-reaches-1b-valuation-in-about-3-months/
- Published: 2026-11-16T23:32:32+00:00
- Summary: Three months since introducing its product, AI cybersecurity startup Corba has raised a $125 million Series A at a $1 billion valuation led by NEA.

### 3. Tech leaders are convinced that Jensen Huang’s exit was a plot against him
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/tech/1035027/tech-leaders-nvidia-jensen-huang-theories
- Published: 2026-11-16T23:17:34+00:00
- Summary: Jensen Huang's stunning resignation from Nvidia after more than 33 years has sent shockwaves throughout the tech industry. Now prominent figures are calling for Huang's reinstatement, and many are also hopping on board with a theory spreading throughout Silicon Valley: that the scandal is the result of a plot against the former CEO. At the [&#8230;]

### 4. QUIC and Covert: Novel HTTP/3-Powered RATs Target Southeast Asian Governments
- Section: Cybersecurity — Research & Threat Intel
- Source: Unit 42 (Palo Alto)
- URL: https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/
- Published: 2026-11-16T23:00:55+00:00
- Summary: We uncover a Southeast Asian cyberespionage campaign deploying PerfectPioneer RAT, modular KUKURAT and stealth HTTP/3 C2 communication channels.
The post QUIC and Covert: Novel HTTP/3-Powered RATs Target Southeast Asian Governments appeared first on Unit 42.

### 5. Gemini AI agents repeatedly bypassed safeguards to attack real website
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/gemini-ai-agents-repeatedly-bypassed-safeguards-to-attack-real-website/
- Published: 2026-11-16T22:54:00+00:00
- Summary: Google's Gemini AI agents repeatedly attempted to hack a real organization's website during AI model safety testing, finding ways to circumvent increasingly restrictive security controls designed to prevent them from accessing live systems. [...]

### 6. Google Project Zero Slashes Bug Disclosure Deadlines, Splitting Experts
- Section: Cybersecurity — Primary
- Source: Dark Reading
- URL: https://www.darkreading.com/vulnerabilities-threats/google-project-zero-bug-disclosure-deadlines
- Published: 2026-11-16T22:08:20+00:00
- Summary: One of the oldest running bug disclosure programs announced it would shorten public disclosure timelines to vendors from 120 days to 30 over the next 14 months.

### 7. All the questions Nvidia should answer on Tuesday — but probably won’t
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/all-the-questions-nvidia-should-answer-on-tuesday-but-probably-wont/
- Published: 2026-11-16T22:03:02+00:00
- Summary: Nvidia interim CEO and longtime CFO Colette Kress is about to have one of the biggest days of her career on Tuesday when the company reports its third-quarter results. Given the turmoil Nvidia is in, there are a number of questions that Nvidia should answer.

### 8. AI Threat Report: How Artificial Intelligence Is Used Across Illicit Communities
- Section: Cybersecurity — Research & Threat Intel
- Source: Flashpoint
- URL: https://flashpoint.io/blog/ai-threat-report-monthly/
- Published: 2026-11-16T22:01:47+00:00
- Summary: A monthly analysis of how artificial intelligence is used in illicit communities, based on Flashpoint proprietary intelligence and direct visibility into real threat actor environments.
The post AI Threat Report: How Artificial Intelligence Is Used Across Illicit Communities appeared first on Flashpoint.

### 9. California sues OpenAI for Hugging Face and other incidents, alleging deception and recklessness
- Section: Cybersecurity — Primary
- Source: The Record (Recorded Future)
- URL: https://therecord.media/california-sues-openai-hugging-face
- Published: 2026-11-16T21:40:00+00:00
- Summary: "OpenAI thwarted the Attorney General’s efforts to investigate these incidents, including by refusing to provide detailed information about the full universe of incidents known to the company,” California alleges in a new lawsuit.

### 10. Google Project Zero cuts bug disclosures to 30 days amid AI threats
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/google-project-zero-cuts-bug-disclosure-deadline-to-30-days-amid-ai-threats/
- Published: 2026-11-16T21:31:44+00:00
- Summary: Google Project Zero will replace its "90+30" disclosure policy with shorter, fixed deadlines in response to AI-accelerated vulnerability discovery and exploitation. [...]

### 11. California sues OpenAI over AI agents escaping sandboxes, hacking firms
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/california-sues-openai-over-ai-agents-escaping-sandboxes-hacking-firms/
- Published: 2026-11-16T20:59:44+00:00
- Summary: California Attorney General Rob Bonta sued OpenAI on Monday, alleging the company knowingly continued testing advanced artificial intelligence models despite repeated security failures that allowed autonomous AI agents to escape isolated environments and launch cyberattacks against real-world organizations. [...]

### 12. California sues OpenAI over rogue AI hacking incidents
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/ai-artificial-intelligence/1034815/california-openai-hugging-face-lawsuit
- Published: 2026-11-16T20:46:01+00:00
- Summary: California is suing OpenAI after its AI agents broke out of their testing environment and hacked other companies, including Hugging Face. In a lawsuit filed Monday, Attorney General Rob Bonta accuses OpenAI of violating consumer safety law by knowingly developing a "dangerous product without proper oversight," as reported earlier by Reuters. The lawsuit claims the [&#8230;]

### 13. Sam Altman says he wants everyone ‘to have a lot of RAM’
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/ai-artificial-intelligence/1034787/sam-altman-ram-shortage-semafor
- Published: 2026-11-16T20:41:28+00:00
- Summary: OpenAI CEO Sam Altman is once again addressing his controversial comments on PC RAM purchases. "I want to be clear, I want people to have a lot of RAM, I think everybody should be able to buy a lot of RAM for their own computer," Altman said today. "I think the home tinkering is great." [&#8230;]

### 14. Big Nuclear isn’t worried about the Democrats stopping data centers
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/science/1034694/nuclear-energy-constellation-earnings-data-centers-democrats
- Published: 2026-11-16T20:29:37+00:00
- Summary: Constellation Energy - America's largest operator of nuclear power plants - does not share Wall Street's concerns that the Democrats will slow down data center development. On the company's third-quarter earnings call last week, CEO Joe Dominguez was, for lack of a better word, unbothered as he addressed the blue wave. "I do think we've [&#8230;]

### 15. US data centers now burn more electricity than a midsized country
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/ai-artificial-intelligence/1034668/data-centers-electricity-climate-pollution-study-harvard
- Published: 2026-11-16T20:27:58+00:00
- Summary: Fossil fuels are still the biggest source of electricity for hyperscale data centers in the US, a new paper published in the journal Nature Sustainability shows. They likely burn through more electricity collectively than many countries do, resulting in a serious amount of greenhouse gas emissions. The study homes in on hyperscale facilities - the [&#8230;]

### 16. Match fined $10 million for alleged Tinder privacy violations
- Section: Cybersecurity — Primary
- Source: The Record (Recorded Future)
- URL: https://therecord.media/ireland-tinder-privacy-fine
- Published: 2026-11-16T20:15:00+00:00
- Summary: Ireland’s data protection regulator will fine the Match Group as a result of the dating app Tinder allegedly failing to provide users with their personal data held by the company upon request.

### 17. California state AG sues OpenAI over rogue agent incidents
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/california-state-ag-sues-openai-over-rogue-agent-incidents/
- Published: 2026-11-16T20:07:13+00:00
- Summary: The California lawsuit represents one of the first attempts to hold an AI lab legally accountable for a rogue agent incident.

### 18. Trump Administration Moves to Block China From Indirect Access to American AI Technology
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/trump-administration-moves-to-block-china-from-indirect-access-to-american-ai-technology/
- Published: 2026-11-16T20:00:00+00:00
- Summary: Under the new rule, overseas data centers that serve companies in countries including China, Russia, Iran and Cuba are required to identify their end users.
The post Trump Administration Moves to Block China From Indirect Access to American AI Technology appeared first on SecurityWeek.

### 19. Barracuda links cloud breach to ARTEX AI-powered cyberattack
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/
- Published: 2026-11-16T19:57:13+00:00
- Summary: Hackers who breached the cloud environment of network and email security company Barracuda earlier this month used a stolen cloud access key and the ARTEX AI penetration testing framework. [...]

### 20. Ransomware Attacks Increase Behind AI, But Payments Decline
- Section: Cybersecurity — Primary
- Source: Dark Reading
- URL: https://www.darkreading.com/threat-intelligence/ransomware-attacks-increase-ai-payments-decline
- Published: 2026-11-16T19:56:05+00:00
- Summary: Large language models and other AI systems allow a growing number of ransomware groups to create convincing phishing emails and identify sensitive data quickly.

### 21. Apple is testing daily usage limits for more complex Siri AI interactions
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/tech/1034581/apple-intelligence-siri-ai-daily-usage-limits-icloud-subscription
- Published: 2026-11-16T19:24:40+00:00
- Summary: Apple released betas of iOS 27.3, iPadOS 27.3, and macOS 27.3 today, and the company is using the update to test new per device daily usage limits for some Siri AI and Apple Intelligence features, according to MacRumors. Basic Siri commands and requests will remain free and unlimited, but more advanced features that rely on [&#8230;]

### 22. OpenAI wants to stop deepfakes from overwhelming child abuse tiplines
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/policy/1034527/openai-csam-classifier
- Published: 2026-11-16T19:23:45+00:00
- Summary: OpenAI is announcing a tool that it says will help child sexual abuse investigators cut through the noise to find harmful material they can act on quickly. At a Monday press briefing in Washington, DC, OpenAI announced a classifier it says can better detect abusive imagery of kids, including whether it's AI-generated. It's also offering [&#8230;]

### 23. Trump says ex-Nvidia CEO Jensen Huang’s affair with an alleged Chinese spy did not threaten national security
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/trump-says-ex-nvidia-ceo-jensen-huangs-affair-with-an-alleged-chinese-spy-did-not-threaten-national-security/
- Published: 2026-11-16T19:12:02+00:00
- Summary: Trump contradicted his own government's intelligence officials, who reportedly concluded that Alice Huang is a Chinese spy.

### 24. 'Sleeper Agent' Tactic Hides Payloads in Open-Weight AI Models
- Section: Cybersecurity — Primary
- Source: Dark Reading
- URL: https://www.darkreading.com/vulnerabilities-threats/sleeper-agent-tactic-payloads-open-weight-ai-models
- Published: 2026-11-16T19:10:03+00:00
- Summary: Malware can lurk inside just 0.00001% of a neural network. How, then, can any user tell it's there?

### 25. Nvidia’s board is reportedly ‘not considering’ hiring Jensen Huang back
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/tech/1034501/nvidia-board-jensen-huang-not-bringing-back
- Published: 2026-11-16T18:43:35+00:00
- Summary: Nvidia's board of directors "isn't considering" having Jensen Huang return as CEO, according to a report from CNBC. A source tells the outlet the board "is focused on an investigation into Huang, and is not in discussions to bring him back." Since Huang's resignation last week, tech executives, along with current and former Nvidia employees, [&#8230;]

### 26. Sam Altman on Nvidia without Jensen Huang: The industry will be ‘fine’
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/sam-altman-on-nvidia-without-jensen-huang-the-industry-will-be-fine/
- Published: 2026-11-16T18:11:10+00:00
- Summary: OpenAI CEO Sam Altman acknowledged the special role Nvidia CEO Jensen Huang has played in the AI boom, but ultimately thinks the industry will be “fine” without him at the helm.

### 27. Italian regulator fines Meta $886 million for violating data privacy law
- Section: Cybersecurity — Primary
- Source: The Record (Recorded Future)
- URL: https://therecord.media/italian-regulator-fines-meta-886-million-privacy
- Published: 2026-11-16T18:05:00+00:00
- Summary: The crackdown on Meta’s Facebook platform involved the company’s alleged use of its “camera roll” suggestions option, launched in 2023, to browse Android users’ photo galleries to recommend posts they could enhance with personal photos and videos.

### 28. AWS Weekly Roundup: AWS Nitro Sandboxes, AWS Emulator, and more (November 16, 2026)
- Section: Cloud Security & Infrastructure
- Source: AWS News Blog
- URL: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-nitro-sandboxes-aws-emulator-and-more-november-16-2026/
- Published: 2026-11-16T17:55:46+00:00
- Summary: A second delivery of the same message can reveal more about an application than its happy-path demo. I like tools that make those cases easier to investigate while a change is still small. Last week’s launch of AWS Emulator brings part of that work onto your own machine: developers and coding agents can exercise AWS […]

### 29. FBI says Artex AI open source hacking tool used to breach networks in ‘under three hours’
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/
- Published: 2026-11-16T17:36:43+00:00
- Summary: The FBI says that the open source hacking tool was used in cyberattacks targeting a U.S. IT giant and the South Korean financial industry.

### 30. King Charles opens new HQ for National Cyber Force, UK’s offensive hacking unit
- Section: Cybersecurity — Primary
- Source: The Record (Recorded Future)
- URL: https://therecord.media/uk-national-cyber-force-headquarters-opens
- Published: 2026-11-16T17:22:00+00:00
- Summary: A building near the Lancashire village of Samlesbury in northwest England is officially the headquarters for the secretive unit that runs the Britain's offensive cyber operations.

### 31. Jordan Belfort’s new AI voice startup, Tone, wants to sell like the ‘Wolf of Wall Street’
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/jordan-belforts-new-ai-voice-startup-tone-wants-to-sell-like-the-wolf-of-wall-street/
- Published: 2026-11-16T17:10:00+00:00
- Summary: Belfort claims his AI sales voice can already close deals almost as well as the best human salespeople, and he thinks it will catch up in a year.

### 32. OpenAI will embed safety researchers to investigate AI subversion
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/
- Published: 2026-11-16T17:02:43+00:00
- Summary: OpenAI will embed six Apollo Research evaluators to investigate whether its AI models engage in subversive behavior, but restrictions on access and disclosure raise questions about their independence.

### 33. Russia denies intercepting Romanian government emails
- Section: Cybersecurity — Primary
- Source: The Record (Recorded Future)
- URL: https://therecord.media/romania-russia-cyberattack-espionage
- Published: 2026-11-16T17:00:00+00:00
- Summary: Russia has denied accusations that its state-backed hackers targeted a Romanian government institution in an attempt to intercept emails exchanged with NATO and the European Union.

### 34. Broadening access to AI for scientists
- Section: AI — Labs & Model Launches
- Source: OpenAI Blog
- URL: https://openai.com/index/expanding-chatgpt-for-academic-researchers
- Published: 2026-11-16T17:00:00+00:00
- Summary: We’re expanding our ChatGPT for Academic Researchers program to offer 200,000 researchers worldwide free access to our frontier models.

### 35. Strengthening the fight against online child sexual abuse with new tools and support
- Section: AI — Labs & Model Launches
- Source: OpenAI Blog
- URL: https://openai.com/index/strengthening-online-child-safety
- Published: 2026-11-16T17:00:00+00:00
- Summary: New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse.

### 36. OpenAI releases a new image classifier and ChatGPT warnings to combat CSAM
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/openai-releases-a-new-image-classifier-and-chatgpt-warnings-to-combat-csam/
- Published: 2026-11-16T17:00:00+00:00
- Summary: ChatGPT will ban an account trying to access CSAM content for 24 hours as a warning.

### 37. Microsoft says months-old bug caused global Microsoft 365 outage
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/microsoft/microsoft-says-months-old-bug-caused-global-microsoft-365-outage/
- Published: 2026-11-16T16:43:24+00:00
- Summary: Microsoft says a software bug introduced in July caused last week's worldwide Microsoft 365 outage, triggering a cascading failure that left more than 80% of its networking gateway servers unresponsive. [...]

### 38. China-Nexus Actors Breach 10 Organizations in AI-Driven Attacks
- Section: Cybersecurity — Primary
- Source: Dark Reading
- URL: https://www.darkreading.com/cyberattacks-data-breaches/china-nexus-actors-breach-10-organizations-ai-driven-attacks
- Published: 2026-11-16T16:36:55+00:00
- Summary: Attackers used Cairn once again in autonomous attacks that targeted advanced manufacturing and defense sectors, as well as civil and human rights organizations.

### 39. Audible turns to AI to help users discover audiobooks
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/audible-turns-to-ai-to-help-users-discover-audiobooks/
- Published: 2026-11-16T15:52:19+00:00
- Summary: Audible's new AI-generated audio previews summarize a book's themes and what readers liked about it, in addition to playing the narrated sample.

### 40. Cursor Supply Chain Attack Started at Fireworks AI
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks/
- Published: 2026-11-16T15:45:43+00:00
- Summary: The attacker stole an access key from Fireworks and used it to exfiltrate credentials that enabled them to push malicious Claude Code extension copies.
The post Cursor Supply Chain Attack Started at Fireworks AI appeared first on SecurityWeek.

### 41. Fandango says hackers stole payment card details from checkout pages
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/fandango-says-hackers-stole-payment-card-details-from-checkout-pages/
- Published: 2026-11-16T15:44:21+00:00
- Summary: Ticket seller Fandango Media is notifying customers about a data breach that exposed payment card details entered on its checkout pages. [...]

### 42. Google Project Zero Sets Course for 30-Day Disclosure Deadline
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/google-project-zero-sets-course-for-30-day-disclosure-deadline/
- Published: 2026-11-16T15:31:25+00:00
- Summary: It will move to a 60-day vulnerability disclosure window in February 2027 and to a 30-day window in January 2028.
The post Google Project Zero Sets Course for 30-Day Disclosure Deadline appeared first on SecurityWeek.

### 43. Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/
- Published: 2026-11-16T15:07:32+00:00
- Summary: Chinese threat actors are broadly adopting the agentic AI penetration testing framework to accelerate their attacks.
The post Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks appeared first on SecurityWeek.

### 44. US tightens AI chip export controls to deter Chinese companies from accessing compute remotely
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-compute-remotely/
- Published: 2026-11-16T15:02:34+00:00
- Summary: Under the interim rule, the U.S. will require firms to get licenses to export AI chips if they may provide compute to China or other restricted countries.

### 45. 7 Tips For Complying with CJIS Password and MFA Requirements
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/7-tips-for-complying-with-cjis-password-and-mfa-requirements/
- Published: 2026-11-16T15:01:11+00:00
- Summary: The FBI's latest CJIS Security Policy requires law enforcement agencies to strengthen password protections and enforce MFA across privileged and non-privileged accounts. Specops Software outlines seven practical steps to meet these requirements, block compromised passwords, and maintain compliance. [...]

### 46. Google Maps can now build trip itineraries with real-time details about each stop
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/google-maps-can-now-build-trip-itineraries-with-real-time-details-about-each-stop/
- Published: 2026-11-16T14:48:13+00:00
- Summary: You could use Ask Maps to plan a holiday shopping day trip or something more complex, like a three-day road trip featuring coastal hikes and oceanfront dining.

### 47. Google Finds Hackers Using AI Agents to Build and Run Exploits From Software Patches
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/11/google-finds-hackers-using-ai-agents-to.html
- Published: 2026-11-16T14:00:00+00:00
- Summary: Google on Monday revealed that adversarial use of artificial intelligence (AI) by threat actors has gone beyond manual prompting to deploying autonomous multi-agent offensive frameworks like ARTEX, CAIRN, CyberStrikeAI, and PentAGI to execute multi-stage intrusions at greater operational velocity.

In tandem, threat actors are leveraging the power and capabilities of large language models (LLMs)

### 48. Google warns that fully-automated AI attacks are coming soon
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/google-warns-that-fully-automated-ai-attacks-are-coming-soon/
- Published: 2026-11-16T14:00:00+00:00
- Summary: Threat actors are now relying on agentic workflows powered by AI-based offensive frameworks to automate vulnerability discovery and exploitation, accelerating attacks to machine speed. [...]

### 49. New Ask Maps features to help with holiday travel and prep
- Section: AI — Labs & Model Launches
- Source: Google AI Blog
- URL: https://blog.google/products-and-platforms/products/maps/ask-maps-holiday-travel-features-2026/
- Published: 2026-11-16T14:00:00+00:00
- Summary: tbd

### 50. Audible is trying to make it easier to find audiobooks you’ll actually like
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/tech/1034083/audible-audio-discovery-ai-feature-availability
- Published: 2026-11-16T14:00:00+00:00
- Summary: Audible is introducing an AI-assisted synopsis feature that's designed to help users determine whether they'll enjoy an audiobook before they jump in and start listening to it. The new audio discovery feature combines audiobook samples, AI overviews, and author commentary to give users more information before choosing their next story, in addition to recommended audiobook [&#8230;]

### 51. Google Maps can now create trip itineraries for you
- Section: AI — News & Analysis
- Source: The Verge AI
- URL: https://www.theverge.com/tech/1034110/google-ask-maps-ai-trip-planning
- Published: 2026-11-16T14:00:00+00:00
- Summary: Google is launching a new AI trip-planning feature for Maps that allows the app to create custom itineraries for you and provide real-time details about each stop. The update, which is rolling out to the Gemini-powered Ask Maps chatbot inside the app, lets you plan a one-day outing or a trip spanning several days. As [&#8230;]

### 52. ⚡ Weekly Recap: N-able 0-Days, Windows 0-Days, Chrome 0-Days, Fridge 0-Days, and More Bad Days
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/11/weekly-recap-n-able-0-days-windows-0.html
- Published: 2026-11-16T13:27:20+00:00
- Summary: A default password opened doors it never should have. A trusted update delivered malware. Even a security feature became a way to break in. Different stories, same problem: the things meant to protect us aren't always doing their job.

Meanwhile, AI is making bug hunting faster, old flaws are still paying off, and attackers keep finding easy ways in. Some attacks take real skill. Others barely

### 53. Microsoft: Windows Server 2016 reaches end of support in 60 days
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-server-2016-reaches-end-of-support-in-60-days/
- Published: 2026-11-16T12:53:18+00:00
- Summary: Microsoft has reminded customers again that Windows Server 2016 will stop receiving security updates after it reaches the end of support in two months. [...]

### 54. Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/telegram-widgets-hit-by-rce-demos-malware-warning-days-after-launch/
- Published: 2026-11-16T12:48:03+00:00
- Summary: Kaspersky suspects exploitation of Telegram’s new widgets to deliver WebRAT, as researchers demo RCE and Pavel Durov disputes the claims.
The post Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch appeared first on SecurityWeek.

### 55. Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html
- Published: 2026-11-16T12:34:21+00:00
- Summary: Six flaws in Danfoss AK-SM800A refrigeration controllers could let a remote attacker take over a controller without logging in, Dutch security consultancy Midnight Blue said earlier this week.

No patch is available, and the researchers say the newest firmware, version 5.4.0, does not fix the flaws.

Government cybersecurity agencies in Belgium, Ireland and Germany told operators this week to

### 56. Retadup Worm Resurfaces 7 Years After Takedown to Spread CoffeeLoader Malware
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/11/retadup-worm-resurfaces-7-years-after.html
- Published: 2026-11-16T12:33:18+00:00
- Summary: Cybersecurity researchers have disclosed details of a new variant of CoffeeLoader, a malware designed to deliver additional payloads to infected machines.

"On launch, the NSIS-based installer executable dropped a file named '7z.dll' into a temporary directory and ran it through rundll32.exe," Kaspersky said in an analysis published today.

"The '7z.dll' file was a patched version of the

### 57. Freshworks alums raise $53M to take on Salesforce, HubSpot with AI-native CRM
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/11/16/freshworks-alums-raise-53m-to-take-on-salesforce-hubspot-with-ai-native-crm/
- Published: 2026-11-16T12:30:00+00:00
- Summary: Dreamteam has signed up more than 100 customers across 13 countries, with some businesses switching from established CRMs.

### 58. Science at the Frontier: How scientists use ChatGPT
- Section: AI — Labs & Model Launches
- Source: OpenAI Blog
- URL: https://openai.com/index/science-at-the-frontier
- Published: 2026-11-16T12:00:00+00:00
- Summary: Explore how more than 1,800 scientists use ChatGPT in research. See findings on daily workflows, reported productivity, and expectations for discovery.

### 59. Australian retail giant Coles investigates cybersecurity incident
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/australian-retail-giant-coles-investigates-cybersecurity-incident/
- Published: 2026-11-16T11:18:09+00:00
- Summary: Coles Group Limited, Australia's second-largest retailer, is investigating what it described as a "cyber security incident" that has not impacted the company's stores. [...]

### 60. Recent UnrealIRCd Vulnerability Exploited in Attacks
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/
- Published: 2026-11-16T11:15:48+00:00
- Summary: Tracked as CVE-2026-114713, the high-severity flaw allows attackers to execute commands with server/IRCOp privileges.
The post Recent UnrealIRCd Vulnerability Exploited in Attacks appeared first on SecurityWeek.

### 61. Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/hackers-probe-newly-disclosed-flaws-in-copeland-refrigeration-controllers/
- Published: 2026-11-16T11:05:42+00:00
- Summary: Vulncheck disclosed 14 vulnerabilities affecting Copeland XWEB EVO controllers, including two that threat actors quickly targeted.
The post Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers appeared first on SecurityWeek.

### 62. Uber Data Breach Impacts 150,000 People
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/uber-data-breach-impacts-150000-people/
- Published: 2026-11-16T11:02:48+00:00
- Summary: Hackers compromised a third-party services provider and stole names, addresses, and driver’s license numbers.
The post Uber Data Breach Impacts 150,000 People appeared first on SecurityWeek.

### 63. Anthropic’s Claude Fable 5.2 blocks fewer security tasks, while Mythos gets better at finding bugs
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/artificial-intelligence/anthropics-claude-fable-52-blocks-fewer-security-tasks-while-mythos-gets-better-at-finding-bugs/
- Published: 2026-11-16T11:00:00+00:00
- Summary: Anthropic recently rolled out Claude Mythos 5.2 to selected partners and Fable 5.2 to regular users, with improvements to coding and reasoning. But we also noticed some interesting cybersecurity changes. [...]
