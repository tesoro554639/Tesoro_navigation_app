import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:tesoro_navigation_app/login_screen.dart';
import 'package:tesoro_navigation_app/register_screen.dart';
import 'package:tesoro_navigation_app/main_screen.dart';

Future<void> loadFonts() async {
  final fontDir = r'C:\Users\Luis James - 554-639\Downloads\flutter\flutter\bin\cache\artifacts\material_fonts';
  
  // Load Roboto font
  final robotoFile = File('$fontDir\\roboto-regular.ttf');
  if (await robotoFile.exists()) {
    final robotoData = await robotoFile.readAsBytes();
    final fontLoader = FontLoader('Roboto');
    fontLoader.addFont(Future.value(ByteData.view(robotoData.buffer)));
    await fontLoader.load();
  }

  // Load MaterialIcons font
  final iconsFile = File('$fontDir\\materialicons-regular.otf');
  if (await iconsFile.exists()) {
    final iconsData = await iconsFile.readAsBytes();
    final iconLoader = FontLoader('MaterialIcons');
    iconLoader.addFont(Future.value(ByteData.view(iconsData.buffer)));
    await iconLoader.load();
  }
}

void main() {
  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    await loadFonts();
  });

  testWidgets('Capture screenshots of auth screens and all four navigation pages', (WidgetTester tester) async {
    tester.view.physicalSize = const Size(480, 960);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(() {
      tester.view.resetPhysicalSize();
      tester.view.resetDevicePixelRatio();
    });

    // 0a. Login Screen screenshot
    await tester.pumpWidget(
      MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          fontFamily: 'Roboto',
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
          useMaterial3: true,
        ),
        home: const LoginScreen(),
      ),
    );
    await tester.pumpAndSettle();
    await expectLater(
      find.byType(LoginScreen),
      matchesGoldenFile('screenshots/00_login_screen.png'),
    );

    // 0b. Register Screen screenshot
    await tester.pumpWidget(
      MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          fontFamily: 'Roboto',
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
          useMaterial3: true,
        ),
        home: const RegisterScreen(),
      ),
    );
    await tester.pumpAndSettle();
    await expectLater(
      find.byType(RegisterScreen),
      matchesGoldenFile('screenshots/00_register_screen.png'),
    );

    // Main App with Navigation Bar
    await tester.pumpWidget(
      MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          fontFamily: 'Roboto',
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
          useMaterial3: true,
        ),
        home: const MainScreen(),
      ),
    );
    await tester.pumpAndSettle();

    // 1. Home Page screenshot
    await expectLater(
      find.byType(MainScreen),
      matchesGoldenFile('screenshots/01_home_page.png'),
    );

    // 2. Calculator Page screenshot
    await tester.tap(find.byIcon(Icons.calculate_outlined));
    await tester.pumpAndSettle();
    await expectLater(
      find.byType(MainScreen),
      matchesGoldenFile('screenshots/02_calculator_page.png'),
    );

    // 3. Profile Page screenshot
    await tester.tap(find.byIcon(Icons.person_outline));
    await tester.pumpAndSettle();
    await expectLater(
      find.byType(MainScreen),
      matchesGoldenFile('screenshots/03_profile_page.png'),
    );

    // 4. Social Media Page screenshot
    await tester.tap(find.byIcon(Icons.share_outlined));
    await tester.pumpAndSettle();
    await expectLater(
      find.byType(MainScreen),
      matchesGoldenFile('screenshots/04_social_media_page.png'),
    );
  });
}
