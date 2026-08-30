# ba_meta require api 9

import babase


# ba_meta export babase.Plugin
class EpicOnslaughtPlugin(babase.Plugin):

    def on_app_running(self) -> None:
        if babase.app.classic is None:
            return
        from bascenev1lib.game.onslaught import OnslaughtGame

        _orig_init = OnslaughtGame.__init__

        def _patched_init(self_inner, settings):
            _orig_init(self_inner, settings)
            self_inner.slow_motion = True

        OnslaughtGame.__init__ = _patched_init

        _orig_spawn = OnslaughtGame.spawn_player_spaz

        def _patched_spawn(self_inner, player, position=None, angle=None):
            spaz = _orig_spawn(self_inner, player, position=position, angle=angle)
            spaz.powerups_expire = False
            spaz.equip_boxing_gloves()
            spaz.default_boxing_gloves = True
            spaz.set_bomb_count(3)
            spaz._max_bomb_count = 3
            return spaz

        OnslaughtGame.spawn_player_spaz = _patched_spawn
