// BMICalculatorTest.java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class BMICalculatorTest {

    @Test
    public void testNormalBMI() {
        assertEquals(22.86, BMICalculator.calculateBMI(70, 1.75), 0.01);
    }

    @Test
    public void testOverweightBMI() {
        assertEquals(27.76, BMICalculator.calculateBMI(85, 1.75), 0.01);
    }

    @Test
    public void testUnderweightBMI() {
        assertEquals(16.33, BMICalculator.calculateBMI(50, 1.75), 0.01);
    }

    @Test
    public void testZeroHeight() {
        assertThrows(IllegalArgumentException.class, () -> {
            BMICalculator.calculateBMI(70, 0);
        });
    }

    @Test
    public void testNegativeHeight() {
        assertThrows(IllegalArgumentException.class, () -> {
            BMICalculator.calculateBMI(70, -1.75);
        });
    }
}