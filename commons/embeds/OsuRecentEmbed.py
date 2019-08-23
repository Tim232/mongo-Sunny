import discord
import commons.osu.classes as osu
import config

class OsuRecentEmbed(discord.Embed):

    def __init__(self, score:osu.Score, beatmap:osu.Beatmap):
        description = f"""
> {score.rank.icon} > **{round(score.performance.pp, 2)}PP """ + (f"({round(score.performance.pp_fc, 2)}PP for {round(score.accuracy(True) * 100, 2)}% FC)" if not score.perfect else "") + f"""** > {round(score.accuracy() * 100, 2)}%
> {score.score} > x{score.maxcombo}/{beatmap.max_combo} > [{score.count300}/{score.count100}/{score.count50}/{score.countmiss}]"""

        if score.performance.completion != 100:
            description += f"""
> **Completion:** {score.performance.completion}%"""

        super().__init__(
            title=discord.Embed.Empty, 
            color=config.getBotConfig().COLOR,
            description=description,
            timestamp=score.date
        )
        
        self.set_author(
            name=f"{beatmap.title} [{beatmap.version}] ({beatmap.creator}) +{str(score.enabled_mods)} [{round(score.performance.star_rating, 2)}★]",
            url=score.server.url_beatmap + str(beatmap.beatmap_id),
            icon_url=score.server.url_avatar + str(score.user_id))
        self.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmap.beatmapset_id}.jpg")
        self.set_footer(text=f"{beatmap.status.name.lower()} | osu! {score.mode.name_full} Play", icon_url=score.mode.icon)