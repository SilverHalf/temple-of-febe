---
layout: page
title: Mechanics
nav_order: 6
has_children: true
---

[Previous](../introduction/lcm.html){: .btn } [Next](empowered.html){: .btn }

# Cerus, the Glaive of House Nephus 

| **Health** | 106,174,800 (CM) or 130,064,136 (LCM) |
| **Armor** |  2597 (standard boss armor) |
| **Instance**| Day |
| **Enrage Timer** | 10 minutes - kills all players on running out. |

The basic gameplay in Temple of Febe is centered around keeping Cerus's attacks as manageable as possible while staying inside of the enrage timer. The fight **becomes progressively more difficult and unforgiving**, due to two important mechanics:

- At the end of each split phase, some of Cerus's recurring attacks will be <img class="inline" src="../images/icons/add_empowered.webp" valign="middle"> buffed. The mechanism for which attacks are selected is deterministic, allowing the group to choose which skills get strengthened and enabling various different strategies.
- On failing certain mechanics, Cerus will gain stacks of <img class="inline" src="../images/icons/empowered.webp" valign="middle"> **Empowered**, which permanently buff his damage.

# Timeline
The encounter consists in **four phases** and **two split phases**.

<div class="container">
	<div class="timeline-item" date-is='100%'>
		<h2>First Phase</h2>
		<p>
			A relatively simple and unpunishing beginning, groups will have no issues here. Make sure you don't fail mechanics and try to phase as fast as possible.
		</p>
	</div>
	<div class="timeline-item" date-is='80% - First defiance bar and split phase'>
		<h2>Second Phase</h2>
		<p>
			A more challenging phase that requires some attention. At points careful positioning is necessary, and there are more opportunities for failure, and graver consequences.
		</p>
	</div>
	<div class="timeline-item" date-is='50% - Second defiance bar and split phase'>
		<h2>Third Phase</h2>
		<p>
			A series of difficult sequences that require careful positioning and timing. Consequences for failure are often fatal, or severly impact the run.
		</p>
	</div>
    <div class="timeline-item" date-is='10% - Final defiance bar'>
		<h2>Final Phase</h2>
		<p>
			The most extreme part of the fight. You are hammered by continuous, increasing, unavoidable damage while having to manage a barrage of relentless attacks.
            Small mistakes can and will kill you, and perhaps your squad as well, but the sensation of getting to the end is glorious.
		</p>
	</div>
</div>

## Arena - the Temple of Febe

The location in which you fight Cerus is the Temple of Febe. It is accessible from the Strike Mission portal in the [Wizard's Tower](https://wiki.guildwars2.com/wiki/The_Wizard%27s_Tower), and can be accessed freely once the [Treachery](https://wiki.guildwars2.com/wiki/Treachery) story step is completed.

![Arena](../images/mechanics/Temple_of_Febe.webp)

Cerus will spawn in the center of this arena, and never moves from there.

In Challenge Mode, any player that falls off the arena is instantly defeated, differently from Normal Mode, where they only take massive damage.

The arena is not one single collision mesh, but many combined. This creates some strange issues with pathfinding, both when dealing with moving [adds]() that spawn throughout the fight, but also when using skills that require an uninterrupted path, such as <img class="inline" src="../images/icons/blink.png" valign="middle"> [Blink](https://wiki.guildwars2.com/wiki/Blink). These skills may not function properly when cast towards or from certain areas of the arena.

## Mitigation Tables

For some attacks analyzed on the following pages, we will highlight how various skills mitigate its effect, shown visually with a table like the following.
<div>
  <ul class="mechtable">
    <li class="table-header">
      <div class="col">
        <img class="table-img" src="../images/icons/distort.png" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/nodmg.png" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/reflect.png" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/dodge.png" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/jump.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/prot.png" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/block.png" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/barrier.webp" valign="middle">
      </div>
    </li>
    <li class="table-row">
      <div class="col">
        <img class="table-img"  src="../images/icons/ok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/ok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/ok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/kinda.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/kinda.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/notok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/notok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/notok.webp" valign="middle">
      </div>
    </li>
    <li class="emp-row">
      <div class="col">
        <img class="table-img"  src="../images/icons/ok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/ok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/ok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/kinda.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/kinda.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/notok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/notok.webp" valign="middle">
      </div>
      <div class="col">
        <img class="table-img"  src="../images/icons/notok.webp" valign="middle">
      </div>
    </li>
  </ul>
</div>
The top header represents various mitigation skills, including  <img class="inline" src="../images/icons/distort.png" valign="middle"> [Distortion](https://wiki.guildwars2.com/wiki/Distortion), Herald's <img class="inline" src="../images/icons/nodmg.png" valign="middle"> [Infuse Light](https://wiki.guildwars2.com/wiki/Infuse_Light), <img class="inline" src="../images/icons/reflect.png" valign="middle"> [Feedback](https://wiki.guildwars2.com/wiki/Feedback) and other projectile mitigation, <img class="inline" src="../images/icons/dodge.png" valign="middle"> [Evasion](https://wiki.guildwars2.com/wiki/Evade), <img class="inline" src="../images/icons/jump.webp" valign="middle"> Jumping, <img class="inline" src="../images/icons/prot.png" valign="middle"> [Protection](https://wiki.guildwars2.com/wiki/Protection), <img class="inline" src="../images/icons/block.png" valign="middle"> [Blocking](https://wiki.guildwars2.com/wiki/Block)/[Aegis](https://wiki.guildwars2.com/wiki/Aegis) and <img class="inline" src="../images/icons/barrier.webp" valign="middle"> [Barrier](https://wiki.guildwars2.com/wiki/Barrier).

The first row represents levels of mitigation for the normal attack. <img class="inline" src="../images/icons/ok.webp" valign="middle"> means that the attack is completely handled by the corresponding skill, <img class="inline" src="../images/icons/kinda.webp" valign="middle"> means the attack is at least partially mitigated, and <img class="inline" src="../images/icons/notok.webp" valign="middle"> means the skill has no effect on the attack. The second row is the same, but for the _empowered_ version (more on this later).

[Previous](../introduction/lcm.html){: .btn } [Next](empowered.html){: .btn }