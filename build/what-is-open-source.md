# What Is Open Source Software?

*Course notes for the lecture "Developing open-source web software: What is open-source software?" These notes go with the slides, and go deeper than them. They're written for students who are about to write about open source themselves, so they explain where the ideas came from, not only what they are. Numbers and versions were checked on 4 November 2026.*

## What we cover

- What open source software is, and what it isn't.
- Where the idea came from: from shared university software, through GNU and the GPL, to Linux, Netscape and the Open Source Initiative.
- *Free software* and its four freedoms, and *open source* and its ten-point definition, and why those are two names for almost the same thing.
- How open source projects are developed: in the open, reviewed by anyone.
- Software licenses: copyleft, permissive, public domain, and Creative Commons for content.
- Examples of open source software you may already use.
- Open source web software: content management systems, and what you need to run them.
- Software frameworks, and how they differ from a CMS.
- Open source compared to proprietary software, and the grey zone in between.
- Quality and security: is open source software any good? (The answer is *njá*. We get there.)

## What is open source software?

Here's a good place to start, from the *Open Source Software Licences User Guide*:

> "Generally, Open Source software is software that can be freely accessed, used, changed and shared (in modified or unmodified form) by anyone."

To understand why that's special, think about how most software reaches you. When you buy a program, or download an app, you get it in a form your computer can run: the *binary*, or *compiled* form. It's a long string of instructions for the processor, and a person can't read it in any useful way. The form a person *can* read, the *source code*, is what the programmers wrote, and that usually stays with the company. You may run the program, under the conditions the company sets in its license agreement, but you can't see how it works, you can't change it, and you can't pass it on.

Open source software turns that around. The source code is published, and its *license* (the legal text that says what you may and may not do with the software) is written to give you rights, not to take them away. You may read the code, run it, change it, and share it, changed or not.

### Source code you can see isn't enough

Despite what the name suggests, software isn't open source because you can see its source code. Plenty of software publishes its code, but doesn't let you use it freely: you may look, but not touch, or you may use it for a hobby but not in a business, or you may change it but not share your changes. That's *source-available* software, and we come back to it at the end of these notes.

For software to be open source, its license has to meet certain conditions. For example:

- The source code is available, to read and to change.
- The software may be passed on without payment, changed or unchanged.
- Changed versions, *derived works*, must be allowed, under the same terms as the original.

That's not a complete list ;-) Two organizations keep the full definitions, and they don't quite agree on the emphasis: the **Free Software Foundation** (FSF), which defines *free software*, and the **Open Source Initiative** (OSI), which defines *open source*. To understand why there are two, we need a little history.

## A short history

### When all software was shared (1950s and 1960s)

In the early days of computing, nearly all software was written at universities and research labs, or by the users of the few computers that existed. Computers were sold, or rented, by companies such as IBM, and the software came with them, often with its source code. Users fixed and improved it, and shared their work with each other. That's how science works: you publish your results, and others build on them.

Users organized themselves to make the sharing easier. SHARE, a user group for IBM's computers, was founded in 1955, and DECUS, for computers from Digital Equipment Corporation, in 1961. They kept libraries of programs that anyone in the group could copy, at first on punched cards and magnetic tapes, later over networks. Nobody called this "open source", or "free software". It was how software worked.

### Software becomes a product (late 1960s to the 1980s)

As more people started writing software, and computers spread from labs into businesses, software started to become a product of its own. In 1969, IBM announced that it would start selling its software separately from its computers ("unbundling"). Other companies followed, and a software industry grew up, writing operating systems, compilers and business programs, and selling *licenses* to use them. This is *proprietary software*: software owned by someone, who decides how you may use it. To protect the product, the source code was kept secret, and by the early 1980s most commercial software came without it.

The story of Unix shows the shift well. Unix was created at AT&T's Bell Labs in 1969, and for years AT&T, which wasn't allowed to go into the computer business, licensed it to universities cheaply, with the source code. Universities studied it, improved it and taught with it; the University of California at Berkeley made its own version, BSD. When AT&T was broken up in 1984, it was free to sell Unix as a product, and the licenses became expensive and restrictive.

### GNU and the Free Software Foundation (1983 to 1989)

Richard Stallman, a programmer at MIT's Artificial Intelligence Lab, had grown up in the sharing culture, and watched it disappear. The story he often tells is of a printer at the lab that jammed all the time. On the lab's previous printer, he had changed the software so it told users when it jammed. For the new one, the manufacturer wouldn't give him the source code, and someone who had it wasn't allowed to share it.

In September 1983, Stallman announced that he would write a complete Unix-like operating system, and give it away to everyone, free to use, study, change and share. He called it **GNU**, a recursive acronym for "GNU's Not Unix" (programmers find that kind of thing very funny). The announcement shook up the software world. In 1985, he published *The GNU Manifesto*, and founded the **Free Software Foundation** to support the work.

One word in Stallman's announcement caused a misunderstanding that has followed us ever since: *free*. In English, "free" means both "free as in freedom" and "free of charge". Stallman meant freedom, and he's been explaining it since: "free as in free speech, not as in free beer". Many other languages have two words for it. In Icelandic, free software is *frjáls hugbúnaður* (free as in freedom), not *ókeypis* (free of charge). In Spanish and French, people say *software libre* and *logiciel libre*, and you'll sometimes meet the acronym FLOSS, "free/libre and open source software", for exactly that reason.

To protect the freedom legally, the FSF wrote a license, the **GNU General Public License**, the GPL. Its first version came out in 1989; version 2 in 1991, and version 3 in 2007. We look at what it says in the section on licenses.

### Linux (1991)

By the early 1990s, the GNU project had written most of an operating system: the compiler, the editor, the command-line tools, the libraries. What it was missing was the *kernel*, the core that talks to the hardware. In 1991, a Finnish student, Linus Torvalds, announced that he was writing a kernel "just a hobby, won't be big and professional". He released it under the GPL the year after. Linux and the GNU tools together made a whole free operating system, which is why the FSF asks that it's called *GNU/Linux*. Most people say *Linux*.

Linux was big and professional after all. Today it runs most of the world's web servers, nearly all of the world's supercomputers, and every Android phone.

### Open source (1998)

In January 1998, Netscape, the company behind Netscape Navigator, one of the first popular web browsers, announced that it would publish the browser's source code. It was losing the "browser war" to Microsoft's Internet Explorer, which came free with Windows. The code was published as the **Mozilla** project in March 1998, and years later it grew into Mozilla Firefox (2004).

Netscape's decision got a group of people in the free software world thinking. They felt that the word "free" scared businesses: it sounded like "no price", or "no value", and the FSF's talk of freedom and ethics sounded like politics. They wanted a name that stressed the practical benefits instead: better software, made together. At a meeting in February 1998, Christine Peterson proposed *open source*, and the name stuck. Eric S. Raymond and Bruce Perens founded the **Open Source Initiative** (OSI) later that month, and published the **Open Source Definition**, based on the guidelines the Debian Linux distribution had written for its own software.

The story is much longer, and I encourage you to read more of it (there are good starting points at the end of these notes). But these are its main pillars.

## Free software: the four freedoms

The FSF defines free software by four freedoms. A program is free software if its users have:

0. **The freedom to run the program as they wish, for any purpose.**
1. **The freedom to study how the program works, and change it to do what they want.** Access to the source code is a precondition for this.
2. **The freedom to redistribute copies, so they can help others.**
3. **The freedom to distribute copies of their changed versions to others.** That way, the whole community gets a chance to benefit from the changes. Access to the source code is a precondition for this too.

Yes, they're numbered from zero. Programmers count from zero ;-)

Note what's *not* in the list: price. Free software may be sold, and selling it is perfectly allowed. In practice it's usually available at no cost too, because anyone who buys a copy may give it away. The licenses the FSF writes, the GPL family, are designed to guarantee these four freedoms.

## Open source: the ten-point definition

The OSI defines open source in ten points, the **Open Source Definition** (OSD). It's about the license the software is distributed under, so every point starts, more or less, with "the license must". Here they are, in my words, with what each one is for.

1. **Free redistribution.** Anyone may sell or give away the software, including as part of a bigger collection of software, and the license may not ask for a fee for that. *So the software can spread.*
2. **Source code.** The program must come with its source code, or there must be a well-publicized way to get it, preferably a free download. The source code must be in the form a programmer would want to work with: no deliberately unreadable code, and no half-compiled intermediate forms. *So you can study and change it.*
3. **Derived works.** The license must allow changes and derived works, and must allow them to be distributed under the same terms as the original. *So improvements can be shared.*
4. **Integrity of the author's source code.** The license may ask that changes are distributed as separate "patch" files next to the original code, and that changed versions carry a different name or version number. *So an author's reputation isn't damaged by someone else's version.*
5. **No discrimination against persons or groups.** Everyone may use the software. *So nobody is excluded.*
6. **No discrimination against fields of endeavor.** The license may not stop anyone from using the software for a particular purpose: in a business, say, or for genetic research. *So "open source, but not for commercial use" isn't open source.*
7. **Distribution of license.** The rights come with the program, to everyone who gets a copy, with no extra license to sign. *So the rights travel with the software.*
8. **License must not be specific to a product.** The rights may not depend on the program being part of a particular software collection. If you take it out and use it on its own, you have the same rights. *So nobody can tie the rights to their product.*
9. **License must not restrict other software.** The license may not place conditions on other software distributed next to it, such as "everything on this disk must be open source". *So open source can live next to anything.*
10. **License must be technology-neutral.** No part of the license may depend on a particular technology, such as "you accept by clicking this button". *So the license works everywhere the software does.*

The OSI reviews licenses against this definition, and keeps a list of the ones it has approved. When people say a license is "OSI-approved", that's what they mean.

## Free software or open source?

So which is it? Two definitions, written by two organizations, for different reasons, and yet they describe almost exactly the same software and the same licenses. The GPL is both a free software license and an open source license. So are MIT, Apache and the rest of the licenses you're likely to meet.

The difference is the *why*. Richard Stallman put it like this:

> "The terms 'free software' and 'open source' stand for almost the same range of programs. However, they say deeply different things about those programs, based on different values. The free software movement campaigns for freedom for the users of computing; it is a movement for freedom and justice. By contrast, the open source idea values mainly practical advantage and does not campaign for principles."

- **Free software** is about ethics. Users ought to control the software they use, and software that takes that control away is a social problem, whatever its quality.
- **Open source** is about practice. Developing software in the open, with anyone able to read and improve it, gives better software, and that's a good reason to do it.

In everyday speech, when I say *open source*, I mean both, and so do most people in the Drupal world. But you should be able to explain the difference, because it's real, and it still shapes debates today, such as whether a license that bans some uses can call itself open source.

## How open source software is made

The licenses make the software free. But most people who hear the words "open source" think of something else: lots of people, working on something together. That's how most open source software is made, and the way of working is as important as the license.

The Icelandic Government Offices (Stjórnarráð Íslands) describe it well (my translation):

> "Open source software is developed with a method that uses distributed review and a transparent process. Distributed review means that every time changes or additions are made to the source code, anyone can look at the changes and review them. Anyone can submit changes and additions, which become part of the software itself if they pass the review process."

> "Open software development could therefore be called democratic software development, because the development itself is based on public participation in the project's decision-making."

In practice, it looks like this, in nearly every big open source project, Drupal included:

- **Everything is public.** The code is in a public repository. Bugs and feature requests are in a public *issue queue*. Discussions happen in public, in the issue queue, in chat channels, and at conferences.
- **Anyone can propose a change.** You make the change on your own copy, and propose it as a *patch* or a *merge request* (also called a *pull request*).
- **Changes are reviewed.** Other people test the change, read the code, and comment. Automated tests run on every change. Only when the change has passed review does a *maintainer*, someone the project trusts with the final say, add it to the software.
- **Credit is public too.** Who did what is recorded, forever, in the project's history. For many developers, their open source work is their CV.

In 1997, Eric S. Raymond wrote an essay comparing two styles of software development: the *cathedral*, built by a small group of experts behind closed doors, and the *bazaar*, noisy, open, with everyone joining in. His conclusion, which he called Linus's law after Linus Torvalds, was: "given enough eyeballs, all bugs are shallow". With enough people looking, someone will find every problem quickly. As we'll see in the section on security, that's true, with one important condition: the eyeballs have to actually be there.

"Democratic" is a nice word, and a little generous. Open source projects are run in many ways: some by a single founder (often called a "benevolent dictator for life"), some by a foundation with an elected board, some by a company. What they share is that the decisions, and the reasons for them, happen in public, and that if the community disagrees strongly enough, it can always take the code and go its own way. That's called a *fork*, and we meet a famous one in the section on web software.

## Software licenses

A license is what makes software free or open source, so let's look at licenses more closely.

### Copyright is the starting point

When someone writes software, they automatically own the *copyright* to it, just as with a book, a photo or a song. Copyright means that nobody else may copy, change or distribute the work without the owner's permission. A license is that permission, in writing: it says what others may do, and on what conditions.

A proprietary license gives you very little: you may run the program, on so many computers, for so long. An open source license gives you everything the definitions above require. Where open source licenses differ is in the *conditions* they attach.

### Copyleft: the freedom travels with the software

The GPL gives you all four freedoms, with one condition: **if you distribute the software, or a changed version of it, you must distribute it under the GPL too, with its source code.** You can't take GPL software, improve it, and sell the improved version as a closed product.

That's called *copyleft*, a play on copyright. Copyleft doesn't do away with copyright; it uses copyright law to keep the software free, where copyright is usually used to restrict it. The freedom travels with the software, to everyone who gets a copy, and everyone who changes it.

Copyleft comes in strengths:

- **Strong copyleft**, the GPL: the whole program, including your changes and anything you combine it with into one program, must be under the GPL when you distribute it.
- **Network copyleft**, the AGPL (Affero GPL): like the GPL, but also counting software that runs on a server and that people use over a network. Under the plain GPL, a company can change GPL software, run it as a web service, and never share its changes, because it never gives anyone a copy. The AGPL closes that gap.
- **Weak copyleft**, the LGPL (Lesser GPL) and the MPL (Mozilla Public License): changes to the library or file itself must be shared, but programs that only *use* it may be under any license. The MPL works file by file: changed MPL files stay MPL, and new files you add can be anything.

Note one important detail: the GPL's condition applies when you **distribute** the software, meaning when you give someone else a copy. Running a website isn't distributing. That's why you can build a website with Drupal (GPL) and keep your site's custom code to yourself, unless you give it to someone else. (This is exactly the gap the AGPL closes.)

### Permissive licenses: do almost anything

**Permissive** licenses, such as MIT, BSD and Apache, let you do almost anything with the software, including using it in a closed, proprietary product, as long as you keep the copyright notice and the license text. The Apache license also has explicit rules about patents: everyone who contributes gives everyone who uses the software a license to their patents on it.

Permissive licenses are popular for code libraries and frameworks, because they make the code easy to use anywhere, with no questions asked. React, Angular, Bootstrap and Symfony are all MIT-licensed.

Neither family is better. They're different choices about what matters most to the people who wrote the software: copyleft protects the freedom of everyone who gets the software in the future; permissive licenses maximize who can use it today.

### Public domain

At the far end are works with no conditions at all: the *public domain*. The **Unlicense** and **CC0** are ways for an author to give up their rights, as far as the law allows (in some countries, including Iceland, authors can't give up all their rights; CC0 then falls back to a license with no conditions, while the Unlicense has no such fallback, which is one reason many lawyers prefer CC0, or MIT).

### Comparing the licenses

These are the licenses on the slide, as choosealicense.com sorts them: from the most conditions to none. Notice that they're not all copyleft: the slide's list goes from strong copyleft, through weak copyleft, to permissive and public domain.

| License | Family | Must share source of changes? | Must use the same license? | Covers use over a network? | Explicit patent grant? |
|---|---|---|---|---|---|
| GNU AGPLv3 | Strong copyleft | Yes | Yes | Yes | Yes |
| GNU GPLv3 | Strong copyleft | Yes | Yes | No | Yes |
| GNU LGPLv3 | Weak copyleft (library) | Yes, for the library | For the library | No | Yes |
| Mozilla Public License 2.0 | Weak copyleft (file) | Yes, for changed files | For changed files | No | Yes |
| Apache License 2.0 | Permissive | No | No | No | Yes |
| MIT License | Permissive | No | No | No | No |
| The Unlicense | Public domain | No | No | No | No |

The GPLv2, which Drupal, WordPress and Linux use, is like the GPLv3 in this table, without the explicit patent grant. Drupal and WordPress are "GPL version 2 or later", meaning you may also use them under version 3. Linux is GPLv2 only.

### Licenses for content: Creative Commons

Text, photos, music and videos have copyright too, and software licenses fit them badly. For those, people use **Creative Commons** (CC) licenses. They're built from a few building blocks:

- **BY**: credit the author.
- **SA** (ShareAlike): share changed versions under the same license (copyleft for content).
- **NC** (NonCommercial): no commercial use.
- **ND** (NoDerivatives): no changed versions.

So CC BY-SA means "credit the author, and share alike". The current version is 4.0. CC licenses with NC or ND aren't open in the sense of the definitions above, because they restrict the use, or the changes. The Drupal site-building book these notes belong to is CC BY-SA 4.0, and so is Wikipedia.

Creative Commons licenses aren't meant for software, and Creative Commons itself recommends against using them for code. Use a software license for code, and a CC license for everything else.

### License compatibility

When you combine code under different licenses into one program, the licenses have to allow it. A permissive license fits inside a GPL project: you may take MIT code and include it in a GPL program, and the whole is distributed under the GPL. It doesn't work the other way: you can't put GPL code in an MIT-licensed program and distribute it as MIT, because the GPL's condition would be broken.

This is why drupal.org only hosts code under the GPL (version 2 or later): every module and theme can be combined with every other, and with Drupal core, without anyone checking licenses first. Drupal itself includes plenty of code under permissive licenses, such as the Symfony framework (MIT).

> **Tip:** choosealicense.com explains the common licenses in plain words, and is a good place to start if you have to choose one for your own project. Each license also has a short, standard identifier, its *SPDX identifier* (such as `GPL-2.0-or-later` or `MIT`), which you'll see in project files.

## Examples of open source software

You probably use open source software every day, whether you know it or not. Here are some well-known examples, each an alternative to a well-known proprietary program.

| Software | Newest version | Designed by | Type | License |
|---|---|---|---|---|
| LibreOffice | 26.8.2 | The Document Foundation (from StarOffice, by Star Division) | Office suite, competing with Microsoft Office | MPL 2.0, with parts also LGPLv3 or later |
| VLC media player | 3.0.24 | VideoLAN | A video player that plays *anything* | GPLv2; libVLC is LGPL 2.1 |
| GIMP | 3.2.8 | The GIMP development team | Image editor, competing with Photoshop | GPLv3 |
| Shotcut | 26.9.27 | Meltytech, built on the MLT framework | Video editor, competing with Premiere | GPLv3 |
| Brave | 1.98.63 | Brave Software | Web browser | MPL 2.0 |
| Linux | Kernel 7.3.1 | Linus Torvalds and the Linux community | Operating system kernel | GPLv2 |

A few notes on the table:

- **Linux** is only the kernel. What you install is a *distribution*, such as Ubuntu, Debian or Fedora, which packages the kernel with the GNU tools and thousands of other programs, and has its own version numbers.
- **LibreOffice** is itself the result of a fork. It started as StarOffice, which Sun Microsystems bought and released as OpenOffice.org. When Oracle bought Sun in 2010, most of the community left and founded The Document Foundation, and LibreOffice.
- **Brave** is built on Chromium, the open source core of Google Chrome. Chrome itself isn't open source: Google adds proprietary parts to it.
- The browser you're probably reading this in is likely to be open source too, or built on open source: Firefox, Chromium, and WebKit, the engine behind Safari.

## Open source web software

### What is it?

*Web software*, for our purposes, is software that publishes web pages and manages the content of websites. The umbrella term, for open source and proprietary software alike, is **CMS**, a *content management system*.

Why do we need a CMS at all? Couldn't we write the pages by hand? You could, and the first websites were written that way. But a modern website isn't a set of pages: it's content (news, events, photos, people) that's stored once and shown in many places, in lists, on the front page, in a search, in a newsletter, in two languages, to some visitors and not others. Content changes every day, and it's edited by people who shouldn't need to know HTML. Nobody hard-codes websites any more. A CMS stores the content in a database and builds the pages from it, every time someone asks for one.

### How many websites are there?

According to Forbes (February 2023), there are about **1.13 billion** websites in the world. In 2006, there were about 100 million, so the number grew almost exponentially for years. The peak was in 2017, with about 1.8 billion websites, and the number has fallen since. Most of those websites are inactive: parked domains, abandoned projects, placeholders. Only a fraction, perhaps 200 million, are active. Still, according to the same source, a new website is built every three seconds!

### What does it take to run open source web software?

Usually, four things, stacked on top of each other:

1. **An operating system**, on the server: Linux, Unix, or Microsoft Windows Server. Most web servers run Linux.
2. **A web server**, the software that receives requests from browsers and sends back pages: Apache and nginx are open source; IIS is from Microsoft. Almost nobody except your system administrator cares which one is used. But the web server does more than send pages: it handles a lot of the security, decides where on the server visitors may and may not go, and where the website's files start (the *web root*).
3. **A database**, to store the content: MySQL, MariaDB and PostgreSQL are open source; Microsoft SQL Server is proprietary. Some systems use *NoSQL* databases, such as MongoDB, which store documents instead of tables.
4. **An interpreter or a runtime**, to run the CMS's code: PHP, Python, Node.js. Not every system is interpreted. Systems written in Java or C# are *compiled* before they run, and need a runtime (the Java virtual machine, or .NET) instead.

The classic open source combination is called **LAMP**: Linux, Apache, MySQL, PHP. Drupal, WordPress and Joomla all grew up on LAMP, and still run happily on it, or on its variations (nginx instead of Apache, MariaDB or PostgreSQL instead of MySQL).

### A story about forks: MySQL and MariaDB

MySQL is a good example of why the open source license matters, and of what a fork is for. MySQL was written in the mid-1990s by the Swedish company MySQL AB, and released under the GPL. It became the "M" in LAMP, the database behind most of the web. (It's named after My, the daughter of one of its authors, Michael "Monty" Widenius.)

In 2008, Sun Microsystems bought MySQL AB, and in 2010, Oracle bought Sun. Oracle sells its own, proprietary database, and many people in the community stopped trusting that MySQL would still be developed with open source in mind. So, in 2009, Monty Widenius took the code and *forked* it: he started a new project from a copy of it, called **MariaDB** (after his younger daughter, Maria). Because MySQL was GPL, nobody could stop him, and MariaDB is GPL too. Many Linux distributions switched to MariaDB, and Drupal supports both.

Forks like this are open source's safety valve. Nobody can take an open source project away from its community, because the community can always take the code and carry on. It has happened again and again: Joomla was forked from Mambo (2005), LibreOffice from OpenOffice.org (2010), and Backdrop CMS from Drupal (2013). Most forks fail, by the way. A fork only survives if enough people follow it.

## Content management systems

Here are some of the best-known open source content management systems.

| System | Newest version | Designed by | Language | Share of all websites |
|---|---|---|---|---|
| WordPress | 7.1.4 | Matt Mullenweg and Mike Little (as a fork of b2/cafelog); today the WordPress community and the WordPress Foundation | PHP | 39.5% |
| Joomla | 6.2.0 | Open Source Matters, Inc. and the Joomla community | PHP | 1.1% |
| Drupal | 11.4.11 (12.0 due Dec 2026) | Dries Buytaert and the Drupal community | PHP | 0.6% |
| Umbraco | 18.3.0 | Niels Hartvig and Umbraco HQ | C# | < 0.1% |
| OpenCms | 22 | Alkacon Software and the OpenCms community | Java | < 0.1% |
| django CMS | 5.1.3 | Divio AG and the django CMS Association | Python (Django) | < 0.1% |
| OpenWGA | 7.12.6 | Innovation Gate GmbH | Java | < 0.1% |

The shares are from W3Techs, which looks at the top 10 million websites. Counting websites is hard, and every survey counts differently, so don't compare numbers from different sources: compare the systems within one source. W3Techs finds no content management system at all on **32.2%** of the websites it looks at. Of the websites whose CMS it can identify, WordPress runs **58.2%**, Joomla 1.6%, and Drupal 0.9%.

So WordPress is far bigger than all the others: about 65 times bigger than Drupal, by this count. That doesn't make it better or worse. WordPress began as a blogging tool, and is unbeatable at getting a simple site up quickly. Drupal began as a community site, and is built for structured content, many editors, many languages, and complex permissions, which is why you find it at universities, governments and large organizations. Each is good at what it's good at. It's never a contest.

Where are the other websites? Many run on proprietary platforms and site builders, such as Shopify, Wix and Squarespace, on custom-built systems, or are static pages with no CMS at all.

### A word about PHP

Most of the big open source content management systems are written in PHP, and PHP is the programming language people love to hate. When they explain why, they usually describe problems from PHP 4 and early PHP 5, twenty years ago. PHP is now at version **8.5.12**, and it's a different language.

PHP was created by Rasmus Lerdorf in 1994, as a set of tools for his personal home page (hence the name, originally "Personal Home Page"). Lerdorf has said he never meant to create a programming language. PHP didn't win because it was the best-designed language; it won because it was everywhere, cheap to host, and easy to start with, and the CMSs built on it brought it to millions of websites.

The turning point came with PHP 5.6 and 7.0 (2015). PHP 6 was never released: it was an ambitious rewrite that was abandoned, and the project jumped straight from 5.6 to 7.0. PHP 7 roughly doubled the speed of most PHP code, and PHP 8 (2020) brought a modern type system, and much more. Today, modern PHP code looks a lot like Java code. The main difference, I tell my students, is the `$` in front of the variable names ;-)

Facebook was famously written in PHP. When it grew, Facebook built its own compiler for PHP (HipHop, then HHVM), and its own dialect of the language, Hack. A lot of Facebook still runs on that lineage.

Is all PHP code well written? No, not always. Sometimes it's horribly written, but that's true of code in every language. I still come across code I wrote a few years ago, and I don't understand what I was doing :-)

## Software frameworks

A *software framework* is a foundation to build software on: a collection of ready-made code for the things nearly every application needs, such as handling web requests, talking to a database, checking who's logged in, and building pages, plus rules for how to structure your own code on top of it.

How does a framework differ from a library, or from a CMS?

- A **library** is code you call when you need it: "format this date". You're in charge.
- A **framework** calls *your* code: you fill in the parts that are specific to your application, and the framework decides when to run them. Programmers call that *inversion of control*.
- A **CMS** is a finished application, built for managing content, often on top of a framework. You configure it, and extend it, but you don't have to write it.

Drupal sits on top of the frameworks: since Drupal 8 (2015), it's been built on components of the Symfony framework. You don't need to know Symfony to build sites with Drupal, but it's there, underneath.

Here are some well-known frameworks. Name a few you've used yourselves!

| Framework | Newest version | Designed by | Language | License |
|---|---|---|---|---|
| .NET | 10.0.14 | Microsoft | C# (and F#, Visual Basic) | MIT, for the open source .NET platform; some tools are proprietary |
| Spring | 7.0.10 | Rod Johnson; today Broadcom (VMware Tanzu) | Java | Apache 2.0 |
| Bootstrap | 5.3.8 | Mark Otto and Jacob Thornton at Twitter; today the Bootstrap core team | HTML, CSS, JavaScript | MIT |
| Angular | 22.2.4 | Google | TypeScript | MIT |
| Django | 6.1.3 | The Django Software Foundation | Python | BSD |
| React | 19.3.1 | Jordan Walke, at Facebook (Meta) | JavaScript | MIT |
| Symfony | 8.1.11 | Fabien Potencier (SensioLabs) and the Symfony community | PHP | MIT |

Two stories from the table:

- **.NET** used to be proprietary, and Windows-only (the .NET Framework). In 2014 Microsoft started releasing a new, cross-platform version as open source, and today's .NET is MIT-licensed. It's a good example of a company changing its mind about open source: in 2001, Microsoft's CEO called Linux "a cancer".
- **React** was first released under a BSD license with an extra patent clause, which said you'd lose your license if you sued Facebook over patents. Many companies, and the Apache Software Foundation, refused to use it. In 2017, Facebook gave in, and relicensed React under MIT. Licenses matter!

## Open source and proprietary software

Here's the comparison from the slides, with some nuance added.

| | Open source | Proprietary |
|---|---|---|
| The code | Open: anyone can read it | Locked away |
| Changes | Anyone may change it | Only the owner |
| Cost | Almost always used without license fees | License fees |
| Bugs | Known: the bug list is public | Unknown: you only know what the vendor tells you |
| The runtime environment | Known, and yours to choose | Often unknown, or decided by the vendor |
| Users | Large user communities, who help each other | Users are not always connected; few user communities |
| Support | From the community, or from companies you pay | From the vendor, as part of what you pay for |
| If the maker stops | Anyone can carry on (fork) | The software dies with the product |

"No license fees" doesn't mean "no cost". You still pay for hosting, for people's time, for support and training. The real difference is who you depend on, and what happens if that relationship ends.

### The grey zone: open core and source-available

Not everything is one or the other.

- **Open core**: the core of the product is open source, and the company sells proprietary extras on top (an "enterprise edition"). GitLab works this way.
- **Source-available**: you can read the code, but the license restricts what you can do with it, so it isn't open source by either definition. In the last few years, several companies switched their open source products to such licenses, to stop cloud providers from selling their software as a service: MongoDB (2018, the SSPL), Elastic (2021), HashiCorp's Terraform (2023, the Business Source License) and Redis (2024).

Each of those switches led to a fork of the last open source version: OpenSearch (from Elasticsearch), OpenTofu (from Terraform) and Valkey (from Redis). And Elastic and Redis later added an open source license (the AGPL) back. The safety valve works.

## Quality and security

### Is open source software worse than proprietary software?

The answer is *njá*. That's an Icelandic word, made of *nei* (no) and *já* (yes): no-but-yes.

Yes, there is badly written open source software. There's badly written software of every kind, and with open source, you get to see it. But open source development is often far ahead of proprietary development, not least because of the number of people who take part. The big projects have more developers, testers and reviewers than most companies could afford, and every change is reviewed in public. Much of the internet runs on open source software (Linux, Apache, nginx, OpenSSL, PHP, Python, MySQL, PostgreSQL), and so do most of the world's biggest companies.

Some of the "no" in *njá*: many small projects are maintained by one or two volunteers in their spare time, and quality varies a lot. Before you depend on an open source project, look at how alive it is: when was the last release, how many people contribute, how quickly are issues answered?

### What about security?

No software is so secure that no security flaws are ever found in it. Neither is a well-built house: windows leak, doors creak. The question is what happens when a flaw is found.

In open source, the flaw is fixed in the open. Well-run projects have a *security team* that receives reports privately, prepares a fix, and then publishes the fix and a *security advisory* at the same time, so everyone can update at once. There is no incentive to hide security flaws, or possible ones, because the code is public, and someone else would find them. They get fixed.

Linus's law, "given enough eyeballs, all bugs are shallow", has a condition, though: the eyeballs have to be there. Three famous cases show what happens when they aren't:

- **Heartbleed** (2014): a serious flaw in OpenSSL, the encryption library behind much of the web's secure connections. It had been in the code for two years. OpenSSL, used by millions of servers, was at the time maintained by a handful of people, with very little funding.
- **Log4Shell** (2021): a flaw in Log4j, a Java logging library used nearly everywhere, maintained by volunteers.
- **The xz backdoor** (2024): someone spent two years earning the trust of the tired, lone maintainer of a small compression library, then hid a backdoor in it. It was caught by chance, by a developer who noticed that his logins had become half a second slower.

Each one led to more funding and more people for the projects that everything else depends on. The lesson isn't that open source is insecure: proprietary software has just as many flaws, and you only hear about them when the vendor decides to tell you. The lesson is that open source is only as healthy as its community, and that's why contributing back matters.

### Drupal and security

Drupal has a dedicated **Security Team**, made of volunteers, which handles security reports for Drupal core and for every contributed module and theme covered by drupal.org's security advisory policy. Fixes are released, with an advisory, on a regular schedule, usually on Wednesdays, so site owners know when to look. If a security flaw in a contributed module isn't fixed, the module is marked *unsupported*, so sites know to stop using it. There are 56,813 modules on drupal.org (counting old and unsupported ones), so that's a lot of code to look after.

A classic joke in Drupal security talks is that `'; DROP DATABASE` doesn't work in Drupal ;) It refers to *SQL injection*, an attack where someone types database commands into a form, hoping the website will run them. Drupal's database layer never puts what users type directly into a database command, so those attacks fail. Well, almost never: in 2014, a flaw in exactly that layer was found, and fixed, in Drupal 7. It became known as "Drupalgeddon", because sites that didn't update within hours were attacked automatically. It's still the best argument for updating quickly.

### Why does Drupal have more (or fewer) security advisories than other projects?

That's one of the questions on the slides, and it's a good one to think about. Some things to consider:

- **What's counted?** Drupal's advisories cover core and contributed projects, and every advisory is published, however small. Other projects may publish only some, or none.
- **More advisories can mean more looking.** A project with an active security team, and a clear way to report flaws, will publish more advisories than one where nobody looks. Zero advisories can be a bad sign.
- **What matters is how flaws are handled:** how fast they're fixed, how clearly they're announced, and how easy it is for site owners to update.

### Two stories

**The White House.** In 2009, whitehouse.gov moved to Drupal. Security was one of the reasons given: with the code open, the government's own experts, and everyone else, could check it, and the community would keep it updated. It was a big moment for open source in government, and many governments followed.

**Mossack Fonseca.** In 2016, the Panama law firm Mossack Fonseca was at the center of the "Panama Papers" leak, 11.5 million documents about offshore companies. Its website ran on WordPress, and its client portal on Drupal. It wasn't WordPress or Drupal that failed: the website used an outdated commercial plugin, Revolution Slider, with a well-known security flaw, and the portal ran a version of Drupal from 2013, open to the Drupalgeddon flaw, which had been fixed in 2014. The lesson: open source or not, software you don't update isn't secure.

## Questions to discuss

These go well in a class discussion, or as starting points for an essay.

1. Is software whose source code you can read, but not change or share, open source? Why not? Find an example of a source-available product, and explain what its license allows.
2. Explain the difference between free software and open source, in your own words. Which of the two do you find more convincing, and why?
3. Choose an open source project you use. What's its license? Is it copyleft or permissive? Who decides what goes into it, and how would you propose a change?
4. A company changes the software it sells as a web service, but never gives anyone a copy. Does it have to share its changes under the GPL? Under the AGPL?
5. Why do you think the big open source content management systems are mostly written in PHP?
6. Find a recent security advisory for an open source project. How was the flaw found, and how long did it take from the report to the fix?
7. *Njá*: argue both sides. When is open source software the better choice, and when isn't it?

## Want to know more?

- *What is Free Software?*, the Free Software Foundation's definition of the four freedoms: <https://www.gnu.org/philosophy/free-sw.html>
- *The Open Source Definition*, from the Open Source Initiative: <https://opensource.org/osd>
- *Why Open Source Misses the Point of Free Software*, Richard Stallman's essay, quoted above: <https://www.gnu.org/philosophy/open-source-misses-the-point.html>
- *The Cathedral and the Bazaar*, Eric S. Raymond's essay: <http://www.catb.org/~esr/writings/cathedral-bazaar/>
- *Choose a License*, the licenses compared: <https://choosealicense.com/licenses/>
- *Is Drupal secure?*, from drupal.org: <https://www.drupal.org/documentation/is-drupal-secure>
- *Licensing FAQ*, from drupal.org: <https://www.drupal.org/about/licensing>
- The numbers in these notes come from W3Techs (<https://w3techs.com>), the projects' own websites and package registries, and Forbes Advisor's website statistics. See `data/numbers.yml` for the source of each one.

---

*These notes, and the slides that go with them, are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). You may share and adapt them, also commercially, as long as you credit the author and share your changes under the same license.*
