---
layout: page
title: Regret
nav_order: 13
parent: Aspects
grand_parent: Mechanics
---

[Previous](despair.html){: .btn } [Next](rage.html){: .btn }

# Crushing Regret

<img class="attack_gif" src="../../images/mechanics/regret.gif">

Spawns a green circle on a random player that explodes after 5 seconds. If there are less than 5 players in its radius, _the entire squad will be instantly defeated_.

The green deals a small amount of unavoidable squad-wide damage, and applies a stack of <img class="inline extreme_vulnerability"> [Extreme Vulnerability] for 3 seconds.

{: .empowered_description }
Three greens will spawn, targeting random different players. Each green is functionally identical to the unempowered version, except it requires at least three people instead of five. Due to <img class="inline extreme_vulnerability"> [Extreme Vulnerability], people who are in the overlap between two greens when they pop will be instantly defeated, colloquially known as getting "Venn Diagrammed".

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
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
    </li>
    <li class="emp-row">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
      <img class="table-img notok">
    </li>
  </ul>
</div>

## Extra Information

- On failure, will technically apply 5 stacks of <img class="inline empowered"> [Empowered] to Cerus, and a stack of <img class="inline exposed"> [Exposed] to every player, like in normal mode.
- Has a maximum range. If you and the green are on opposite sides of the arena, you won’t die if it fails.
- **BUG:** the green circle has a visual radius of 240, but its actual radius is 360.

## Strategy

Managing the normal version of this attack is trivial.

The empowered version requires special attention. The most common strategy is to divide the squad into 3 groups of at least 3 people. Each group has a designated “Anchor” player and a designated “Runner” player, with the third player being the “Backup”. The 10th player is an optional “Float”.

In the following image, the first row represents the Anchors, the second the Backups, and the last one the Runners and Floats, while the columns represent individual groups.

![Green Strategy](../../images/mechanics/green_strat.webp)

The Anchors are usually [marked](https://wiki.guildwars2.com/wiki/Commander#Markers), and spread out to pre-established locations before each green mechanic, with their groups following them. When greens appear, if more than one green spawns inside of a group, the people targeted move to other groups, and the Runners from the other groups move back to cover the resulting gap. Runners should always be the first player to move in case of overlapping greens. Anchors should never move. Backups only move if both they and their Anchor have a green.

Proper prepositioning before each green is crucial for this strategy to work. Any confusion regarding which green belongs to which group can be fatal.

Correct and reliable execution of Empowered Regret is one of the major hurdles for any progression groups that choose to face this mechanic.

[Previous](despair.html){: .btn } [Next](rage.html){: .btn }

[Empowered]: https://wiki.guildwars2.com/wiki/Empowered_(Cerus)
[Exposed]: https://wiki.guildwars2.com/wiki/Exposed
[Extreme Vulnerability]: https://wiki.guildwars2.com/wiki/Extreme_Vulnerability