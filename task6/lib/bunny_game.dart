import 'dart:ui';
import 'helpers/directions.dart';
import 'package:flame/game.dart';
import 'bunny_player.dart';
import 'bunny_world.dart';

class DinoGame extends FlameGame{
  DinoPlayer _dinoPlayer = DinoPlayer();
  DinoWorld  _dinoWorld = DinoWorld();
  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_dinoWorld);
    await add(_dinoPlayer);
    _dinoPlayer.position = _dinoWorld.size / 1.5;
    camera.followComponent(_dinoPlayer,
        worldBounds: Rect.fromLTRB(0, 0, _dinoWorld.size.x, _dinoWorld.size.y));
  }
  onArrowKeyChanged(Direction direction){
      _dinoPlayer.direction = direction;
    }
  
}
