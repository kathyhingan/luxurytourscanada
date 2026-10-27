# DNS cutover runbook: luxurytourscanada.com to GitHub Pages

DONE 2026-10-27, verified by Hermes the same day: apex resolves to the four
185.199.x.153 A records, www CNAME resolves to kathyhingan.github.io,
Let's Encrypt cert issued (valid 2026-10-26 to 2027-01-24), Enforce HTTPS
ticked on the Pages settings, www 301s to the apex, all 20 sitemap URLs
return 200 with self-canonicals, and the capture E2E re-ran green from the
live origin (fetch probe ok:true). Steps below kept for the record.

Written 2026-10-24 from live DNS state. The domain is PURCHASED and parked:

- Nameservers: dns1.registrar-servers.com, dns2.registrar-servers.com
  (registrar default DNS)
- Apex A record: 162.255.119.27 (registrar parking page, not GitHub Pages)
- https://luxurytourscanada.com: no response yet
- Repo: local only, no GitHub remote yet
- CNAME file: in the repo root, content luxurytourscanada.com, added
  2026-10-24 (the build docs referenced it before it existed; fixed)

Registrar read: those nameservers plus that parking IP are the default pair
Namecheap hands out, so the click path below is written for Namecheap. If the
dashboard looks different, the records themselves are identical; only the
screen names change.

## Order matters (zero-downtime sequence)

Publish the site first (repo plus Pages), then touch DNS last. Cutting DNS
before Pages serves the domain sends visitors to a 404.

## Step 1: create the GitHub repo and push (Kathy, 5 minutes)

The sibling sites live at github.com/kathyhingan (arkipelago,
bestcateringphilippines). Same pattern here:

1. Log in at github.com as kathyhingan.
2. New repository. Name: luxurytourscanada. Public (Pages on the free plan
   needs public; the sibling repos are the same). No README, no gitignore, no
   license: this repo ships its own files. Create.
3. In Terminal:

   ```
   cd ~/Documents/ops-automation-icm/repos/luxury-tours-canada
   git remote add origin https://github.com/kathyhingan/luxurytourscanada.git
   git push -u origin main
   ```

   The local branch is main (checked 2026-10-24), so no rename needed.
4. Refresh the GitHub page: the pages, assets folder, CNAME and robots.txt
   must all be listed at the repo root.

## Step 2: enable Pages with the custom domain (Kathy, 2 minutes)

1. Repo page > Settings > Pages (left rail).
2. Source: Deploy from a branch. Branch: main, folder: / (root). Save.
3. Same screen, Custom domain: type luxurytourscanada.com > Save. GitHub
   shows a DNS check pending. Expected until Step 3 lands.
4. Leave Enforce HTTPS OFF for now; GitHub issues the certificate only after
   DNS points here. Tick it in Step 5.

## Step 3: the four A records plus www CNAME (Kathy, 5 minutes)

In the registrar: Domain List > Manage next to luxurytourscanada.com >
Advanced DNS.

1. DELETE the existing A record pointing at 162.255.119.27 (the parking
   record). It is the only record to remove.
2. ADD four A records, host @, TTL Automatic, the GitHub Pages apex IPs:

   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

3. ADD one CNAME record: host www, target kathyhingan.github.io., TTL
   Automatic.
4. Save. On default registrar DNS this usually propagates within minutes.

## Step 4: verify (Hermes or Kathy, 2 minutes)

```
dig +short luxurytourscanada.com A
# expect the four 185.199.x.153 addresses
dig +short www.luxurytourscanada.com
# expect kathyhingan.github.io.
curl -sI https://luxurytourscanada.com | head -3
# expect HTTP 200 and server: GitHub.com
```

## Step 5: close out (Kathy)

1. GitHub > Settings > Pages: tick Enforce HTTPS once the certificate is
   issued (can take up to a day after DNS lands).
2. Confirm the green custom-domain check on the same screen.

## Rollback

The only record removed is the parking A. To go back: restore one A record,
host @, value 162.255.119.27. The domain returns to the parked page. Nothing
else was changed anywhere.
