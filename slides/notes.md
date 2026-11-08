# Speaker notes: What is open-source software?

The speaker notes for `slides/template.pptx`, one section per slide. `tools/build.py` puts them into the deck, so edit them here, not in the deck. Placeholders such as {{ php }} come from `data/numbers.yml`. A slide with no section gets no notes. Lines starting with `- ` become their own paragraph, as in the rest of the notes.

## Slide 4

Despite the wording, which might suggest otherwise, having the source code available doesn't necessarily make software open source. For that, it has to meet certain conditions.

Software can be called open if it meets conditions such as these:

- The source code is available, to read and to change.
- It may be passed on without payment, changed or unchanged.
- Derived software must be allowed under the same terms as the original.

Not a complete list ;-)

## Slide 5

There's a difference in ideological emphasis between these two terms, and you need to look into both of them, since your essay is partly about them. In everyday speech, when I say "open source", I mean both free software and open source software. The two are closely tied together, but there is a fundamental difference between them, and you need to be able to tell them apart.

A little history. Let's go back to the 1950s and 1960s, when the idea of shared software took shape. Universities and research labs wrote almost all the software at the time, and they shared it among themselves, as is the way in that community. Software was passed around freely, through user groups (such as SHARE, for IBM computers), on tapes, and later on network servers, available to everyone, without conditions.

Then time passed, more people started writing software, and things changed a lot at the end of the 1960s, when companies started writing operating systems and compilers and general software, and charging for it. In 1969, IBM started selling software separately from its computers. That's how proprietary software came about: companies sold licenses to use their software, and kept the source code to themselves.

Up until 1983, there was no movement for free software. The idea was there, and many would have liked to work that way, but it was too costly. Then, in September 1983, Richard Stallman announced that he would write a Unix-like operating system, called GNU, a recursive acronym for "GNU's Not Unix", and that it would be free for everyone. That announcement really shook up the software community. In 1985 he founded the Free Software Foundation (FSF), and in 1989 the first GNU General Public License (GPL) was published. In 1991, Linus Torvalds released the Linux kernel, which, together with the GNU tools, made a whole free operating system.

The wording in Stallman's announcement was unfortunately ambiguous, because "free" in English means both "free as in freedom" and "free of charge". That misunderstanding has followed us ever since. Stallman's own way of putting it: "free as in free speech, not as in free beer".

The term "open source" came about in 1998. Netscape, best known for Netscape Navigator, one of the first web browsers, decided to release the browser's source code. It came out first under the name Mozilla, and later grew into Mozilla Firefox. Later that same year, the term "open source" was coined, the Open Source Initiative (OSI) was founded, and more companies followed. The story is longer, of course, and I encourage you to read more about it. But these are the main pillars in the history of open source.

## Slide 6

The licenses published by the FSF follow these rules.

The four freedoms of software:

- 0. The freedom to run the program as you wish, for any purpose.
- 1. The freedom to study how the program works, and change it to suit your needs.
- 2. The freedom to redistribute copies, so you can help others.
- 3. The freedom to improve the program and share your changes, so the whole community benefits.

## Slide 7

Open source is defined in 10 points, the Open Source Definition (OSD), by the OSI. It was written in
1998. It builds on the FSF's definitions, but there are differences.

## Slide 8

Open source doesn't just mean access to the source code. The distribution terms of open source software must comply with the following criteria (summarized from the Open Source Definition, opensource.org/osd):

1. Free redistribution. The license may not stop anyone from selling or giving away the software as part of a bigger distribution with programs from several sources, and may not require a royalty or other fee for such a sale.

2. Source code. The program must include source code, and must allow distribution in source code as well as compiled form. Where a product is not distributed with source code, there must be a well-publicized way to get it for no more than a reasonable copying cost, preferably downloading it from the internet for free. The source code must be the form a programmer would prefer to change. Deliberately obfuscated source code is not allowed, nor are intermediate forms such as the output of a preprocessor or translator.

3. Derived works. The license must allow changes and derived works, and must allow them to be distributed under the same terms as the license of the original software.

4. Integrity of the author's source code. The license may stop source code from being distributed in changed form only if it allows "patch files" to be distributed with the source code, to change the program at build time. The license must explicitly allow distributing software built from changed source code. It may require derived works to carry a different name or version number from the original.

5. No discrimination against persons or groups. The license must not discriminate against any person or group of persons.

6. No discrimination against fields of endeavor. The license must not stop anyone from using the program in a specific field. For example, it may not stop the program from being used in a business, or for genetic research.

7. Distribution of license. The rights attached to the program must apply to everyone it is redistributed to, without them needing to get an additional license.

8. License must not be specific to a product. The rights attached to the program must not depend on it being part of a particular software distribution. If the program is taken out of that distribution and used or distributed under the program's license, everyone it is redistributed to has the same rights as those granted with the original distribution.

9. License must not restrict other software. The license must not place restrictions on other software distributed along with it. For example, it may not insist that all other programs distributed on the same medium are open source.

10. License must be technology-neutral. No part of the license may be based on an individual technology or style of interface.

## Slide 9

Open source follows a certain set of rules. One definition of open source software can be found on the website of the Icelandic Government Offices (Stjórnarráð Íslands); the quotes on this slide are translated from it.

Most people who hear the term "open source" think of exactly this: we're all working on something together.

The freedom then comes into open source through the software licenses.

## Slide 10

All of these are open source alternatives to well-known proprietary software. Ask the class: which of these have you used, and did you know they were open source?

The Linux version is the kernel's; distributions such as Ubuntu and Fedora have their own version numbers.

Look at the licenses: most are GPL, a copyleft license. LibreOffice and Brave use the MPL, a weaker, file-level copyleft. Versions checked on {{ checked }}.

## Slide 11

Copyleft is a play on copyright: it uses copyright law to keep software free, where copyright is usually used to restrict it.

Show the licenses in the browser (choosealicense.com/licenses).

Open source licenses grant permission for anybody to use, modify, and share licensed software for any purpose, subject to conditions preserving the provenance and openness of the software. The following licenses are sorted by the number of conditions, from most (GNU AGPLv3) to none (Unlicense). Notice that the popular licenses featured on the home page (GNU GPLv3 and MIT) fall within this spectrum.

So not all of these are copyleft. The GNU licenses are (the LGPL more weakly), the MPL is a weak, file-level copyleft, Apache and MIT are permissive, and the Unlicense is as close to public domain as a license gets. Creative Commons licenses are made for content, such as text, photos and course material, not for code.

## Slide 12

There's a lot of open source web software out there, and I'm only dipping my big toe in by naming some of them, but these are some of the biggest.

What is open source web software? Software to publish web pages and manage the content of websites. The umbrella term for this kind of software, open and proprietary alike, is CMS: content management system.

Question: how many websites are there in the world today? According to Forbes (February 2023), there are about {{ websites_total }}! In 2006 there were only about 100 million, so the number grew almost exponentially in 17 years. The peak was in 2017, with about 1.8 billion websites, so the number has dropped by almost 700 million since then.

Question: which websites are visited the most? Google and YouTube. Then come the three social media sites, Facebook, Instagram and Twitter (X), and WhatsApp was in tenth place (2023).

A new website goes live every three seconds!

Web servers are the software underneath websites. Apache and nginx are open source; IIS is from Microsoft. Almost nobody but your system administrator cares which web server is used. But the web server doesn't only serve the page: it handles a lot of the security, where you may and may not go (in the folder structure, for example), and where the web root is. We look at web servers a little when we look at DDEV, a tool bundle for web development.

We also need a database under the website, to store the content. Nobody hard-codes websites any more. An interesting story about open source: MySQL was open source, made by the Swedish company MySQL AB. Sun Microsystems bought MySQL AB in 2008, and Oracle bought Sun in 2010. At that point, people stopped trusting that MySQL would still be developed with open source in mind. So Michael "Monty" Widenius, one of MySQL's original authors, split the code off (a fork) into MariaDB.

An interpreter isn't always used. Sometimes web systems are written in Java or C#, and then the system is compiled, not interpreted.

## Slide 13

NOTE: All of these are open source. There are others out there that are proprietary, or custom-built.

The share column is the share of all websites, from W3Techs, which looks at the top 10 million websites ({{ checked }}). W3Techs finds no content management system at all on {{ share_no_cms }} of them. Where are the rest? Custom-built systems, static sites, and proprietary site builders and platforms such as Wix, Squarespace and Shopify.

WordPress is about 65 times bigger than Drupal ({{ share_wordpress }} vs. {{ share_drupal }} of all websites). Among websites with a CMS we can identify, WordPress has {{ cms_share_wordpress }}.

PHP is the programming language people love to hate. And they recite problems from versions 4 to 5.4. PHP is now at version {{ php }}! The turning point came with versions 5.6 and 7.0, and there's been no looking back since.

PHP didn't win because it was "better": Rasmus Lerdorf, who created it, has said he was really waiting for someone to come up with something better. The point is that PHP is the dominant language for open source content management systems.

PHP 6 went down the drain: we went straight from 5.6 to 7.0. Version 6 was so great, so much was rewritten… that it was thrown away.

The difference between Java and PHP 8 is almost nothing. The main difference between the two languages is the $ in front of variable names.

PHP is by far the most popular language for web systems, both open and custom-built. Facebook was for a while written entirely in PHP. Later they built their own compiler for it (HipHop, then HHVM) and their own PHP dialect (Hack), but a lot of it is still in that lineage.

Are they well written? No, not always. Sometimes the code is horribly written, but that's true of all software. I still come across code I wrote a few years ago, and I just don't understand what I was doing :-)

django CMS doesn't publish its usage numbers, but it's still under active development: it is now at version {{ django_cms }}.

## Slide 17

The answer is "njá", an Icelandic word that means no-but-yes (nei + já). Of course there is badly written open source software, as there is badly written software of every kind. But open source development is often far ahead of proprietary development, not least considering the number of people writing it.

About 35,000 people take part regularly in the Drupal community, of whom about 3,500 write code for Drupal core.

No software is so secure that no security flaws are ever found. No more than well-built houses: windows leak, doors creak, and so on.

But then they get fixed. The same goes for open source. Security releases for zero-day vulnerabilities are well known, and people are asked to update right away. There is no incentive to hide security flaws, or possible ones. They just get fixed. And if a security flaw is found in a contributed module and isn't fixed, the module is marked unsupported, so sites know to stop using it.

There are {{ drupal_modules }} modules for Drupal on drupal.org (counting old and unsupported ones). The Drupal Security Team handles security reports for every project covered by the security advisory policy. "; DROP DATABASE doesn't work in Drupal ;)

Drupal was chosen for the White House website (whitehouse.gov, from 2009), partly because of security.

Mossack Fonseca, the law firm at the center of the Panama Papers leak (2016), ran its website on WordPress. It wasn't WordPress core that failed, but an outdated plugin with a known security flaw (Revolution Slider, a commercial plugin). Its client portal also ran an outdated version of Drupal (7.23), open to the "Drupalgeddon" flaw fixed in 2014. The lesson: keep everything updated.
