---
layout: page
title: Regret
nav_order: 13
parent: Aspects
grand_parent: Mechanics
---

[Previous](despair.html){: .btn } [Next](rage.html){: .btn }

# Regret - Crushing Regret
{: .center}

<img class="divider">

<img class="attack_gif" src="../../images/mechanics/regret.gif">

<div class="smalltext center">GIF credit: Snowcrows</div>

<img class="divider">

Spawns a green circle on a random player that explodes after 5 seconds. If there are less than 5 players in its radius, it will <img class="inline down"> [Downstate] every player and give them a stack of <img class="inline exposed"> [Exposed], and Cerus will gain 5 stacks of <img class="inline empowered"> [Empowered].

The green also deals a small amount of unavoidable squad-wide damage, and applies a stack of <img class="inline extreme_vulnerability"> [Extreme Vulnerability] for 3 seconds. 

{: .empowered_description }
Three greens will spawn, targeting random different players. Each green is functionally identical to the unempowered version, except it requires at least three people instead of five. Players who recieve two stacks of <img class="inline extreme_vulnerability"> [Extreme Vulnerability] due to being in two greens at the same time will be put into <img class="inline down"> [Downstate]. People who take three stacks due to being in three greens will be instantly defeated.

{: .legendary}
Failing a green will instantly defeat the entire squad. Players who recieve two stacks of <img class="inline extreme_vulnerability"> [Extreme Vulnerability] will be instantly defeated.

<div>
  <ul class="mechtable">
    <li class="table-header">
      <img class="table-img distort">
      <img class="table-img glint_h">
      <img class="table-img feedback">
      <img class="table-img dodge">
      <img class="table-img jump">
      <img class="table-img protection">
      <img class="table-img block">
      <img class="table-img barrier">
    </li>
    <li class="table-row">
      <img class="table-img notok">
      <img class="table-img kinda1">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
    </li>
    <li class="emp-row">
      <img class="table-img notok">
      <img class="table-img kinda1">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
    </li>
  </ul>
</div>

1. _Only in normal CM_, effects that prevent lethal damage (<img class="inline aed"> [A.E.D.](https://wiki.guildwars2.com/wiki/A.E.D.), <img class="inline rebound"> [Rebound!](https://wiki.guildwars2.com/wiki/%22Rebound!%22), <img class="inline reversal"> [Reversal of Fortune](https://wiki.guildwars2.com/wiki/Reversal_of_Fortune)) will allow a player to not get downed by a failed green. These effects will not function in case of multiple failed greens: players will stil down to two, and die to three. However, direct damage-to-healing conversion, such as <img class="inline glint_h"> [Infuse Light](https://wiki.guildwars2.com/wiki/Infuse_Light) or <img class="inline defiant"> [Defiant Stance](https://wiki.guildwars2.com/wiki/Defiant_Stance), _will_ prevent downing from multiple green failures.
<div class="smalltext">Thanks to @mashi for helping me test this!</div>

## Extra Information

- Has a maximum range. If you and the green are on opposite sides of the arena, you won’t die if it fails.
- In normal CM, current hypothesis is that failed greens deal a massive amount of damage that ignores all forms of <img class="inline determined"> [Invulnerability]. This would enable them to ignore <img class="inline down"> [Downstate], and has the side effect of also invalidating other forms of player invulnerability.
- This is the only one of Cerus's Aspect attacks that does not have any associated voice lines.

## Strategy

Managing the normal version of this attack is trivial, however the <img class="inline empowered_add"> Empowered version, known as "triple greens" is one of the most difficult mechanics in the entire game, and is rarely seen outside of title runs.

The most common strategy for triple greens is to divide the squad into 3 groups of at least 3 people. Each group has a designated “Anchor” player and a designated “Runner” player, with the third player being the “Backup”, and the 10th player the “Float”.

In the following image, each circle represents a player, with the first row being the Anchors, the second the Backups, and the last one the Runners and Floats, while the columns represent individual groups.

![Green Strategy](../../images/mechanics/green_strat.webp)
<div class="smalltext center">Image credit: @Luna</div>

The Anchors are usually [marked](https://wiki.guildwars2.com/wiki/Commander#Markers), and spread out to pre-established locations before each green mechanic, with their groups following them. When greens appear, each player acts according to their role:

- **Anchors** - never move from their stack after reaching their position.
- **Runners** - If they have a green, and there are multiple greens in their stack, they move to a stack where there is no green. If their stack has no greens, and another has multiple, they move to the other one.
- **Backups** - If they have a green and their anchor has a green, they move to a stack where there is no green. Otherwise, they remain with their stack.
- **Float** - If they have a green, they move to a stack with no green. Otherwise, they can back up for a dead or unavailable player, or provide additional security in case of confused situations.

Proper prepositioning before each green is crucial for this strategy to work, as any confusion regarding which green belongs to which group can be fatal.

An emerging strategy is to have multiple [Tempests] using <img class="inline rebound"> [Rebound!](https://wiki.guildwars2.com/wiki/%22Rebound!%22) as backup for failed greens, especially in the final 10% phase. Players can then stack multiple greens and survive.

[Previous](despair.html){: .btn } [Next](rage.html){: .btn }

[Empowered]: https://wiki.guildwars2.com/wiki/Empowered_(Cerus)
[Exposed]: https://wiki.guildwars2.com/wiki/Exposed
[Extreme Vulnerability]: https://wiki.guildwars2.com/wiki/Extreme_Vulnerability
[Downstate]: https://wiki.guildwars2.com/wiki/Downed
[Invulnerability]: https://wiki.guildwars2.com/wiki/Invulnerability
[Tempests]: https://wiki.guildwars2.com/wiki/Tempest